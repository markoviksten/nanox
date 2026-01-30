# RAGAS-testituloksien Analyysi ja Optimointiehdotukset

## 📊 Yhteenveto tuloksista
- Kokonaisarvio: Erinomainen pohja tuotantoon. Suurin kehityskohde on Vastauksen relevanssi (0.6888), joka laahaa muun laadun perässä ja aiheuttaa konkreettisia virheitä (mm. linkki- ja sisältöhallusinaatiot).
- Taulukko metriikoista (tulos, tavoite, status)

| Metriikka | Tulos | Tavoite | Status |
|---|---:|---:|:--:|
| Totuudenmukaisuus | 0.8711 | ≥ 0.90 | ⚠️ |
| Vastauksen relevanssi | 0.6888 | ≥ 0.85 | ❌ |
| Kontekstin kattavuus | 0.9259 | ≥ 0.90 | ✅ |
| Kontekstin tarkkuus | 0.8318 | ≥ 0.85 | ⚠️ |
| RAGAS-keskiarvo | 0.8294 | ≥ 0.85 | ⚠️ |
| Kustannus/testi | $0.0400 | ≤ $0.05 | ✅ |
| Input-tokenit | 221,544 | -25–40% | ⚠️ |

### Keskeiset havainnot
- ✅ Vahvuudet
  - Erittäin hyvä kontekstin kattavuus (0.9259): relevantit lähteet löytyvät.
  - Korkea totuudenmukaisuus (0.8711): generointi hyödyntää kontekstia pääosin oikein.
  - Kustannustaso matala per testi.

- ⚠️ Kehityskohteet
  - Vastauksen relevanssi (0.6888): vastauksiin päätyy kysymykseen kuulumattomia lisätietoja ja virheellisiä yksityiskohtia.
  - Kontekstin tarkkuus (0.8318): mukana on joskus liikaa tai sivuavaa kontekstia, joka sekoittaa generaatiota.
  - Yksittäiset virheet: URL-hallusinaatiot (login.netvisor.fi vs suomi.netvisor.fi), extra-sisältö (esim. “kuljetetun tavaran määrä”), väärä viittauslähde (YouTube-linkit), epämääräiset vastuut (yhteystiedot).

## 🎯 Pääongelma
- Yksityiskohtainen ongelman kuvaus
  - Relevanssi jää matalaksi, koska generaattori ei ole riittävän vahvasti “ankkuroitu” kontekstiin. Tämä johtaa:
    - URL- ja lähdehallusinaatioihin, kun malli täydentää muististaan (esim. Testi #3: login.netvisor.fi vs GT: suomi.netvisor.fi; Testi #15: ohjeiden lähteeksi dokumentti, vaikka GT vaatii YouTube-linkit).
    - Off-topic-lisäyksiin, jotka eivät vastaa kysymykseen (Testi #4: osallistujien lisäksi “kuljetetun tavaran määrä”).
    - Epätarkkoihin tulkintoihin erityisehdoista (Testi #11: poikkeustilanteiden korvaukset kuvattu yleisesti eikä GT:n rajauksen mukaan).
  - Retrieval tuo kattavan materiaalin, mutta chunkit ovat osin liian laajoja ja re-rankkaus ei aina nosta täsmällisintä pätkää ylimmäksi → generaattori poimii vääriä yksityiskohtia.
  - Prompt ei kiellä eksplisiittisesti keksittyjä linkkejä/termejä eikä pakota vastausta rajatusti “vain kontekstista”.

- Konkreettiset esimerkit
  - #3 URL: “https://login.netvisor.fi” vs GT: “https://suomi.netvisor.fi”
  - #4 Off-topic: osallistujat → lisätty “kuljetetun tavaran määrä”
  - #11 Yleistys: korvausperiaatteet kuvattu yleisesti, ei GT:n tapausta vasten
  - #15 Lähde: dokumentti vs GT: YouTube-linkit
  - #18 Vastuuroolit: epämääräinen, ei GT:n mukaisia selkeitä ohjaavia rooleja

## 🔧 Optimointiehdotukset
- Priorisoidut toimenpiteet (P1, P2, P3)
- Jokaiselle: ongelma, ratkaisu, koodi, arvioitu vaikutus

1) P1: “Vain kontekstista” -prompt + URL-/lähde-whitelist-guardrail
- Ongelma: Generaattori lisää keksittyjä linkkejä/termejä ja ylitulkitsee.
- Ratkaisu: 
  - Prompt, joka:
    - Saa vastata vain kontekstissa esiintyvillä faktoilla, URL:illa ja termeillä.
    - Kieltää ulkoiset lähteet ja arvaamisen; jos tieto puuttuu, palauttaa “Ei löydy kontekstista”.
  - Post-prosessor, joka pudottaa vastauksesta kaikki URL:it ja viittaukset, joita ei löydy kontekstista (whitelist).
- Koodi (Python, esimerkkirunko):

```python
import re

ALLOWED_URL_PATTERN = re.compile(r'https?://[a-z0-9\.\-_/]+', re.I)

def extract_allowed_urls(contexts: list[str]) -> set[str]:
    urls = set()
    for c in contexts:
        urls.update(ALLOWED_URL_PATTERN.findall(c))
    return urls

def strip_disallowed_urls(answer: str, allowed: set[str]) -> str:
    def repl(m):
        url = m.group(0)
        return url if url in allowed else ''
    return ALLOWED_URL_PATTERN.sub(repl, answer)

PROMPT = """
Vastaa VAIN alla olevasta kontekstista löytyviin tietoihin. 
- Älä käytä mallin muistia.
- Käytä vain kontekstissa esiintyviä URL-osoitteita, koodeja ja termejä.
- Jos vastausta ei löydy kontekstista, vastaa: "Ei löydy kontekstista."

Konteksti:
{context}

Kysymys:
{question}

Muotoile vastaus suoraan kysymykseen, ilman ylimääräistä taustoitusta.
"""

def generate_answer(llm, contexts, question):
    allowed_urls = extract_allowed_urls(contexts)
    context_text = "\n---\n".join(contexts)
    raw = llm.invoke(PROMPT.format(context=context_text, question=question))
    clean = strip_disallowed_urls(raw, allowed_urls)
    return clean.strip()
```

- Arvioitu vaikutus: 
  - Vastauksen relevanssi +0.10–0.18
  - Kontekstin tarkkuus +0.03–0.06
  - URL-hallusinaatiot ~0 → 0

2) P1: Cross-encoder re-rankkaus + pienemmät chunkit (vähemmän “sivuääntä”)
- Ongelma: Liian laajat chunkit ja pelkkä vektorihaku tuovat mukaan sivuavaa sisältöä.
- Ratkaisu:
  - Pilko dokumentit 300–500 tokenin chunkkeihin, 60–80 tokenin overlap.
  - Käytä cross-encoder -re-ranker (esim. ms-marco-MiniLM-L-6-v2) top-50 vektorihakutuloksen päälle, valitse top-5.
- Koodi:

```python
from sentence_transformers import CrossEncoder

reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def rerank(query: str, passages: list[str], top_k: int = 5):
    pairs = [(query, p) for p in passages]
    scores = reranker.predict(pairs)
    ranked = sorted(zip(passages, scores), key=lambda x: x[1], reverse=True)
    return [p for p, s in ranked[:top_k]]
```

- Arvioitu vaikutus:
  - Vastauksen relevanssi +0.08–0.12
  - Kontekstin tarkkuus +0.04–0.07
  - Input-tokenit −10–20% (vähemmän turhaa kontekstia)

3) P2: MMR-kontekstikompressio + “evidence highlighting” mallille
- Ongelma: Vaikka oikea chunk löytyy, mukana on vielä redundanttia tekstiä.
- Ratkaisu:
  - Käytä MMR:ää (diversiteetti) top-k valintaan.
  - Tuota mallille “evidence only” -tiivistelmä (lauseet, joissa vastauksen kannalta oleelliset avainsanat).
- Koodi (MMR):

```python
import numpy as np

def mmr(query_vec, doc_vecs, docs, k=5, lambda_mult=0.7):
    selected, candidates = [], list(range(len(docs)))
    selected_scores = []

    sim_to_query = np.dot(doc_vecs, query_vec)
    while len(selected) < k and candidates:
        mmr_scores = []
        for c in candidates:
            if not selected:
                diversity = 0
            else:
                diversity = max([np.dot(doc_vecs[c], doc_vecs[s]) for s in selected])
            score = lambda_mult * sim_to_query[c] - (1 - lambda_mult) * diversity
            mmr_scores.append((c, score))
        c_best = max(mmr_scores, key=lambda x: x[1])[0]
        selected.append(c_best)
        candidates.remove(c_best)
    return [docs[i] for i in selected]
```

- Arvioitu vaikutus:
  - Relevanssi +0.03–0.06
  - Tokenit −10–15%

4) P2: Intent- ja domain-reititys (HR/Matkalasku/Työaika)
- Ongelma: “mix”-tilassa kysymykset voivat osua väärään dokumenttialueeseen.
- Ratkaisu:
  - Luokittele kysymys intenttiin (esim. “Matkalasku/URL”, “Työaika-kirjaus”, “Päivärahat”) ja ohjaa domain-kohtaiseen indeksiin/rerankkeriin.
- Koodi (kevyt luokitin, esimerkki):

```python
import re

def route_domain(query: str) -> str:
    q = query.lower()
    if re.search(r'(matkalasku|päiväraha|kilometri|kuitti|netvisor.*(suomi|login))', q):
        return "travel_expense"
    if re.search(r'(työaika|kirjaa|minuutit|seuranta|poissaolo|vuosiloma)', q):
        return "time_tracking"
    return "general_hr"

# käytä domain-kohtaista retrieveriä
```

- Arvioitu vaikutus:
  - Relevanssi +0.04–0.08

5) P3: KKnowledge base -hygienia ja canonical mapping
- Ongelma: Dokumenteissa esiintyy useita URL-muotoja ja termejä.
- Ratkaisu:
  - Lisää canonical mapping (esim. suomi.netvisor.fi) indeksiin ja promptiin näkyvän whitelistin lähteeksi.
  - Enrichaa dokumentteja metadatalla (url=canonical, doc_type, valid_from/valid_to).
- Koodi (URL normalisointi indeksoinnissa):

```python
CANONICAL = {
    "netvisor_login": "https://suomi.netvisor.fi",
}

def normalize_urls(text: str) -> str:
    return text.replace("https://login.netvisor.fi", CANONICAL["netvisor_login"])
```

- Arvioitu vaikutus:
  - Hallusinaatioiden väheneminen (URL) → lähes 0
  - Relevanssi +0.02–0.04

6) P3: “Ei löydy kontekstista” -fallback ja vastauspituusrajat
- Ongelma: Pitkät, ympäripyöreät vastaukset → relevanssi laskee.
- Ratkaisu:
  - Jos evidenssiä < kynnys, palauta fallback.
  - Rajoita vastaus 2–5 bulletiin, suora vastaus ensin.
- Koodi:

```python
def answer_or_fallback(contexts, question, llm, min_evidence_len=50):
    if sum(len(c) for c in contexts) < min_evidence_len:
        return "Ei löydy kontekstista."
    return generate_answer(llm, contexts, question)
```

- Arvioitu vaikutus:
  - Relevanssi +0.03–0.05
  - Totuudenmukaisuus +0.02–0.03

## 📈 Implementointijärjestys ja vaikutusarviot
- Taulukko: prioriteetti, työmäärä, vaikutus

| Toimenpide | Prioriteetti | Työmäärä | Vaikutus laatuun | Vaikutus kustannuksiin/latenssiin |
|---|:--:|:--:|:--:|:--:|
| “Vain kontekstista” -prompt + URL guardrail | P1 | 0.5–1 pv | ★★★★☆ (Relevanssi) | ~0 |
| Cross-encoder re-rankkaus + chunkkaus | P1 | 1–2 pv | ★★★★☆ | +10–20% latenssi |
| MMR-kompressio + evidence highlighting | P2 | 1 pv | ★★★☆☆ | −10–15% tokenit |
| Intent/domain-reititys | P2 | 1 pv | ★★★☆☆ | ~0 |
| Canonical URL -normalisointi | P3 | 0.5 pv | ★★☆☆☆ | ~0 |
| Fallback + pituusrajat | P3 | 0.5 pv | ★★☆☆☆ | −5–10% tokenit |

Arvio: Relevanssi 0.6888 → 0.84–0.88 yhdistämällä P1 + P2. RAGAS-keskiarvo > 0.86.

## 🚀 Pika-voitot (Quick Wins)
- Ota käyttöön “Vain kontekstista” -prompt ja URL-whitelist-guardrail (koodi yllä) ✅
- Chunkkaa dokumentit 300–500 tokeniin ja pienennä top_k=3–5 kontekstiksi ✅
- Lisää vastauspituusrajat: “vastaa 2–5 bulletilla, älä lisää ylimääräistä taustaa” ✅
- Canonicalisoi Netvisor-URL: “https://suomi.netvisor.fi” indeksoinnissa ja vastauksissa ✅
- Lisää “Ei löydy kontekstista” -fallback, jos evidenssi heikko ✅

## 🔬 A/B-testaussuunnitelma
- Tavoite: Nostaa Vastauksen relevanssi ≥ 0.85 ilman totuudenmukaisuuden heikkenemistä.
- Koeasetelma:
  - Populaatio: 150–300 HR/Netvisor-kysymystä (syntettinen + aidot anonyymisoidut kysymykset).
  - Jaottelu: 50/50 Baseline vs Variantti (P1 + re-rankkaus). Stratifikoi intentin mukaan (Matkalasku, Työaika, Poissaolot).
  - Mittarit:
    - RAGAS: Answer Relevance (primääri), Faithfulness, Context Precision/Recall
    - Hallusinaatioaste: osuus URL:ista, joita ei löydy kontekstista (tavoite 0%)
    - Tokenit/kysymys ja latenssi
  - Menetelmä: Interleaved evaluation + bootstrap-luottamusvälit. 95% luottamustaso.
  - Kesto: 3–5 arkipäivää liikennevolyymin mukaan.
- Pysäytyskriteerit:
  - Relevanssi +≥0.10 parannus ja Faithfulness ±0.00–0.02 sisällä (ei heikkenemistä).
  - Ei merkittävää latenssipiikkiä (>25%).

## 📊 Monitorointi ja jatkuva parantaminen
- Jatkuva RAGAS-ajo:
  - Päivittäinen batch 50 satunnaistetulle kysymykselle, tallennus mlflow/warehouse.
  - Hälytys, jos:
    - Relevanssi < 0.80 2 peräkkäisenä päivänä
    - Hallusinaatio-URL-aste > 0.5%
- Telemetria:
  - Logita: kysymys, top-k kontekstit, valittu evidenssi, vastaus, käytetyt URL:t, latenssi, tokenit.
- Driftin seuranta:
  - Dokumenttien versiointi (valid_from/valid_to), varoitus jos kontekstista löytyy ristiriitaisia URL-muotoja.
- Säännölliset korjaukset:
  - Viikkokatselmoidaan heikoimmat 10 vastausta; lisätään testikantaan regressiotesteiksi.
- Automatisoitu validointi (esim. URL-politiikka):
  - Regex-tarkastus CI-putkessa: vastaus ei saa sisältää URL:ia, joita ei löydy kontekstista.

## 📝 Yhteenveto
- Nykytila
  - Korkea kontekstin kattavuus ja hyvä totuudenmukaisuus. Relevanssi jää jälkeen, mikä näkyy konkreettisina virheinä (URL-hallusinaatiot, off-topic-lisät).
- Pääongelma
  - Generointi ei ole riittävän ankkuroidusti kontekstissa; re-rankkaus ja chunkkaus eivät vielä tee tarpeeksi selektiivistä evidenssin valintaa.
- Ratkaisu
  - P1: “Vain kontekstista” -prompt + URL-whitelist-guardrail ja cross-encoder re-rankkaus sekä pienemmät chunkit. P2: MMR-kompressio ja domain-reititys. P3: Canonical URL -normalisointi ja fallbackit.
- Odotettu tulos
  - Vastauksen relevanssi 0.84–0.88, RAGAS-keskiarvo > 0.86, URL-hallusinaatiot ~0, tokenit −15–30%.
- Seuraavat askeleet
  - (1) Ota käyttöön P1-toimet ja päivitä tuotantoprompti + guardrail-koodi.
  - (2) Ota käyttöön re-rankkaus ja chunkkaus; laske top_k=3–5.
  - (3) Käynnistä A/B-testi (150–300 kysymystä, 3–5 pv).
  - (4) Implementoi monitorointi ja hälytykset.
  - (5) Laajenna P2-toimiin (MMR, domain-reititys) testitulosten perusteella.