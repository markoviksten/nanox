# RAGAS-testituloksien Analyysi ja Optimointiehdotukset

## 📊 Yhteenveto tuloksista
- Kokonaisarvio
  - Jakautumat (kysymystyypit ja chunk-määrät) osuvat hyvin tavoitteisiin.
  - Testikysymysten laatu kuitenkin kärsii sisällöllisistä duplikaateista, katkaistuista ground truth -teksteistä (”...”) ja rajallisesta monihyppyisyydestä (3–5 chunkin aidosti vaativat kysymykset).
  - Tämä testijoukko todennäköisesti yliarvioi RAG-järjestelmän suorituskykyä (RAGAS-metriikoissa), koska vaikeat/kontrastiset ja harhauttavat testit puuttuvat.

- Taulukko metriikoista (tulos, tavoite, status)

| Metriikka | Tulos | Tavoite | Status |
|---|---:|---:|:--:|
| Kysymystyyppien jakauma (short/reason/synth) | 29.2% / 41.7% / 29.2% | 30% / 40% / 30% | ✅ |
| Chunk-jakauma (1/2/3/4/5) | 20.8/20.8/22.9/20.8/14.6% | 20/20/25/20/15% | 🟡 (3-chunk −2.1%) |
| Duplikaattiaste (sisällölliset) | arviolta 30–35% | < 10% | 🔴 |
| Ground truth -täydellisyys (ei ”...”) | arviolta 15–25% katkaistu | 0% katkaisua | 🔴 |
| Aidosti monihyppyiset kysymykset (≥3 chunk) | arviolta 10–15% | ≥ 30% | 🔴 |
| Aihediversiteetti (Netvisor vs. muut) | Selvästi Netvisor-painotteinen | Tasapainoisempi | 🟡 |
| Tokenit/kysymys (kokonais) | ~2344 | < 1500 | 🟡 |
| Kustannus/kysymys | ~$0.00046 | < $0.001 | ✅ |
| Generointiaika/kysymys | ~5.8 s | < 6 s | ✅ |

### Keskeiset havainnot
- ✅ Vahvuudet
  - Jakaumat noudattavat tavoitetta lähes täsmälleen (sekä kysymystyypeissä että chunk-määrissä).
  - Kustannus ja läpimenoaika ovat erinomaisia tähän volyymiin.
  - Kysymykset heijastelevat oikeita järjestelmätermejä (esim. Netvisor-työvaiheet, ”pakolliset kentät”, ”pankkitunnuksilla”).
- ⚠️ Kehityskohteet
  - Sisällölliset duplikaatit: useita lähes saman kysymyksen variaatioita (esim. lomien ja poissaolojen kirjaaminen Netvisorissa).
  - Ground truth -vastaukset useissa kohdissa katkaistuja (”...”), mikä heikentää evaluoinnin luotettavuutta ja RAGAS faithfulness -tulkintaa.
  - Monihyppyisyyden puute: valtaosa kysymyksistä ratkeaa yhdestä lähteestä; harhauttavia konteksteja ei ole.
  - Aihediversiteetti kapea: painottuu työaikaseurantaan/lomiin/matkalaskuihin; vähemmän sääntötulkintoja, poikkeustilanteita ja numerisia reunaehtoja.
  - Token-efektiivisyys: ~2344 tokenia/kysymys → voidaan kiristää ilman laadun alenemista.

## 🎯 Pääongelma
- Yksityiskohtainen ongelman kuvaus
  - Testijoukko ei riittävästi stressaa RAG-pinoa. Kun kysymykset ovat toistensa parafraaseja ja ratkeavat yksittäisestä chunkista, retrieverin ja rerankerin puutteet eivät näy RAGAS-metriikoissa (context_precision, context_recall, faithfulness). Puuttuvat hard-negatives ja monihyppyisyys johtavat liian optimistisiin arvioihin.
  - Katkaistut ground truth -tekstit (”...”) estävät luotettavan faithfulness-arvioinnin, koska odotettu vastaus ei ole yksiselitteinen eikä täydellinen.
- Konkreettiset esimerkit
  - Duplikaatit/variaatiot:
    - Q1, Q6, Q7, Q10, Q12, Q14: ”Miten lomat/poissaolot kirjataan Netvisorissa?” vain pienin muunnelmin.
    - Q21, Q23, Q26, Q28, Q31, Q34: toistavat samaa teemaa (miksi kirjata lomat/poissaolot Netvisoriin).
  - Katkaistut ground truthit:
    - Useita rivejä, esim. Q1, Q2, Q3, Q4 (”...”), jolloin tarkka odote ja mahdolliset numeriset ehdot puuttuvat.
  - Monihyppyisyyden puute:
    - Vaikka osa kysymyksistä on merkitty 3–5 chunkiksi, vastaus ei edellytä yhdistelyä (usein toisteinen selite samasta prosessista).

## 🔧 Optimointiehdotukset
- Priorisoidut toimenpiteet (P1, P2, P3)
- Jokaiselle: ongelma, ratkaisu, koodi, arvioitu vaikutus

1) P1: Testiaineiston rakenteellinen parannus (deduplikointi, täydet ground truthit, hard-negatives)
- Ongelma: Korkea duplikaattiaste, katkaistut ground truthit, helppoja yksichunk-kysymyksiä.
- Ratkaisu:
  - Deduplikoi kysymykset semanttisesti (clustering, threshold 0.88 cosine).
  - Täydennä ground truth -vastaukset 1–2 ytimekkääseen, täydelliseen kappaleeseen ja lisää viitteet chunk_id-listana.
  - Luo 20–30% testijoukosta ”hard-negative” -asetuksilla: lisää sekaan tarkoituksella hyvin samankaltaisia mutta virheellisiä konteksteja, ja arvioi context_precision.
- Koodi (deduplikointi ja GT-korjaus, esimerkki):
```python
# pip install sentence-transformers rapidfuzz pandas
from sentence_transformers import SentenceTransformer
from rapidfuzz import fuzz
import pandas as pd
import numpy as np

df = pd.read_json("nano_2advanced_testcases_aligned.json")  # columns: ["question","ground_truth","chunks",...]

# 1) Semanttinen deduplikointi
model = SentenceTransformer("intfloat/multilingual-e5-base")
emb = model.encode(df["question"].tolist(), normalize_embeddings=True, batch_size=64, show_progress_bar=True)

# Pairwise lähestymistapa (nopea karsinta)
def cosine(a, b): return np.dot(a, b)

keep = []
removed = set()
for i in range(len(df)):
    if i in removed:
        continue
    keep.append(i)
    for j in range(i+1, len(df)):
        if j in removed:
            continue
        sim = cosine(emb[i], emb[j])
        if sim >= 0.88:
            # varmistetaan ettei ole vain lyhyt muutos (Levenshtein/ratiosim)
            if fuzz.token_sort_ratio(df.loc[i,"question"], df.loc[j,"question"]) >= 85:
                removed.add(j)

df_dedup = df.iloc[keep].reset_index(drop=True)

# 2) Ground truth -katkaisujen korjaus: poistetaan rivit, joissa '...' ja merkitään täydennettäväksi
def needs_fix(gt: str) -> bool:
    return "..." in gt or len(gt.strip()) < 20

df_dedup["gt_needs_fix"] = df_dedup["ground_truth"].apply(needs_fix)
df_fix = df_dedup[df_dedup["gt_needs_fix"]]

# -> Täydennä df_fix rivit ohjelmallisesti (LLM) tai käsin, ja lisää viitteet: df_dedup["ground_truth_citations"] = [[chunk_ids],...]
df_dedup.to_json("testcases_clean.json", orient="records", force_ascii=False, indent=2)
```
- Arvioitu vaikutus:
  - RAGAS faithfulness ja relevancy tulkinta muuttuu realistisemmaksi (vähemmän ”helpohkon” testin biasia).
  - Context_precision/recall erotteleva voima kasvaa (hard-negatives).
  - Duplikaattiasteen lasku < 10% → parempi peitto.

2) P1: Hybrid retrieval + rerankkaus käyttöön ennen seuraavaa evaluointia
- Ongelma: Vaativammat (3–5 chunk) kysymykset edellyttävät tarkkaa hakua; nykyinen testijoukko ei paljasta virheitä, mutta tuotannossa ne korostuvat.
- Ratkaisu:
  - Ota käyttöön BM25 + Dense -yhdistelmähaku sekä cross-encoder-rerankkaus (bge-reranker-v2) top-20 → top-5.
- Koodi (LangChain-miniesimerkki):
```python
# pip install langchain faiss-cpu sentence-transformers rank_bm25
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.retrievers import BM25Retriever, EnsembleRetriever
from sentence_transformers import CrossEncoder

docs = [...]  # list of Documents (page_content, metadata)
emb_model = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-base")
vs = FAISS.from_documents(docs, emb_model)
dense_retriever = vs.as_retriever(search_type="similarity", search_kwargs={"k": 20})
bm25_retriever = BM25Retriever.from_documents(docs)
bm25_retriever.k = 20

ensemble = EnsembleRetriever(retrievers=[bm25_retriever, dense_retriever], weights=[0.5, 0.5])

# Cross-encoder reranker
reranker = CrossEncoder("BAAI/bge-reranker-v2-m3")

def retrieve(query, top_k=5):
    cands = ensemble.get_relevant_documents(query)
    pairs = [[query, d.page_content] for d in cands]
    scores = reranker.predict(pairs)
    ranked = [d for _, d in sorted(zip(scores, cands), key=lambda x: x[0], reverse=True)]
    return ranked[:top_k]
```
- Arvioitu vaikutus:
  - +10–25% context_precision ja +5–15% context_recall vaativissa multichunk-kysymyksissä.
  - Faithfulness paranee, kun huonoja (mutta läheisiä) osumia putoaa pois.

3) P2: Chunkkaus ja päällekkäinen kontekstihallinta
- Ongelma: Yhdessä chunkissa on mahdollisesti liikaa heterogeenista sisältöä; monihyppyisyys ei synny luonnostaan.
- Ratkaisu:
  - Ota käyttöön semanttinen segmentointi (600–800 tokenia, 20–30% overlap), ja korosta metadataa (otsikko, alaotsikko) embeddingeissä.
- Koodi (yksinkertaistettu split + overlap):
```python
# pip install tiktoken
import tiktoken

def tokenize(text, model="gpt-4o-mini"):
    enc = tiktoken.get_encoding("cl100k_base")
    return enc.encode(text)

def chunk_text(text, max_tokens=800, overlap=200):
    toks = tokenize(text)
    chunks = []
    start = 0
    while start < len(toks):
        end = min(start + max_tokens, len(toks))
        chunk = toks[start:end]
        chunks.append(chunk)
        start = end - overlap
        if start < 0: start = 0
        if end == len(toks): break
    return chunks
```
- Arvioitu vaikutus:
  - Lisää aidosti yhdisteltäviä pätkiä → kasvattaa monihyppyisten kysymysten laatua ja nostaa context_recallia.

4) P2: Kysymysgeneraation ohjaus: pakota monihyppyisyys ja numeriset reunaehdot
- Ongelma: Kysymykset toistavat samaa teemaa eivätkä vaadi laskentaa/ristiriitojen ratkaisua.
- Ratkaisu:
  - Prompt-säännöt: vähintään 30% kysymyksistä vaatii kahden eri dokumenttiosan yhdistelyä; vähintään 20% sisältää numerisia ehtoja (esim. kesto, prosentit, koodit).
  - Lisää ”disambiguation”-kysymyksiä (samankaltaiset termit eri järjestelmissä).
- Koodi (generaattoripromptin skeleton, OpenAI):
```python
# pip install openai
from openai import OpenAI
client = OpenAI()

system = """Laadi 48 testikysymystä seuraavilla ehdoilla:
- type distribution: short 30%, reasoning 40%, synthesis 30%
- chunks: 1:20%, 2:20%, 3:25%, 4:20%, 5:15%
- vähintään 30% kysymyksistä vaatii yhdistelyä ≥2 erillisestä chunkista
- vähintään 20% sisältää numeerisia ehtoja (koodit, päivät, prosentit, rajat)
- lisää 20% disambiguation-kysymyksiä, joissa kaksi samankaltaista käsitettä erotetaan
- vältä semanttisia duplikaatteja (cosine sim < 0.85 aiempiin)
Palauta jokaiselle kysymykselle täydellinen ground truth ja lista viite-chunk_id:istä.
"""

resp = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role":"system","content":system},{"role":"user","content":"Käytä lähdettä vdb_chunks.json (tiivistelmät metadatasta)."}],
    temperature=0.4
)
```
- Arvioitu vaikutus:
  - Nostaa RAGAS faithfulnessin erottelua (vähemmän helppoja, enemmän tarkkuutta vaativia tapauksia) ja lisää testien realistisuutta.

5) P3: Vastauspromptin guardrailit ja pituusohjaus
- Ongelma: LLM voi tuottaa hallusinaatioita tai laveita vastauksia, mikä sekoittaa faithfulnessin.
- Ratkaisu:
  - Lisää sääntö: jos konteksti ei riitä, palauta ”INSUFFICIENT_CONTEXT”.
  - Pituusohjaus: short_factual ≤ 2 lausetta; reasoning 3–6; synthesis 5–8 + lähdeviitteet.
- Koodi (vastauspromptin runko):
```python
RAG_SYSTEM_PROMPT = """
Vastaa ainoastaan annetuista konteksteista. Jos tieto ei löydy varmasti, palauta 'INSUFFICIENT_CONTEXT'.
- short_factual: max 2 lausetta
- reasoning: 3-6 lausetta, perustele viittauksin
- synthesis: 5-8 lausetta, yhdistä useita lähteitä ja lisää [chunk_id:t]
Älä lisää ulkoista tietoa.
"""
```
- Arvioitu vaikutus:
  - Faithfulness kasvaa, context_precision paranee (vähemmän ylimääräistä), ja mittaus on vakaampi.

6) P3: Token-efektiivisyys ja kustannusten optimointi
- Ongelma: ~2344 tokenia/kysymys voidaan supistaa.
- Ratkaisu:
  - Kontekstin tiivistys ennen mallille syöttöä (MMR-trimmi, duplikaattikatkaisu), vastauspituusrajat, cache.
- Koodi (MMR-trimmi):
```python
from langchain.retrievers import MMRRetriever

mmr_retriever = vs.as_retriever(search_type="mmr", search_kwargs={"k": 20, "fetch_k": 50, "lambda_mult": 0.5})
```
- Arvioitu vaikutus:
  - −20–35% tokenit/kysymys ilman vastauslaadun heikkenemistä.

## 📈 Implementointijärjestys ja vaikutusarviot
- Taulukko: prioriteetti, työmäärä, vaikutus

| Prioriteetti | Toimenpide | Työmäärä | Vaikutus RAGAS-metriikoihin |
|---|---|---:|---:|
| P1 | Deduplikointi + GT-täydennys + hard-negatives | 2–4 pv | Faithfulness/Precision +15–30% |
| P1 | Hybrid retrieval + cross-encoder rerank | 2–3 pv | Context_precision +10–25%, Recall +5–15% |
| P2 | Chunkkaus (800 tok, 20–30% overlap) | 1–2 pv | Recall +5–10% monihypyissä |
| P2 | Generointipromptin sääntöjen tiukennus | 0.5–1 pv | Vaikeustaso ↑, mittauksen erottelu ↑ |
| P3 | Guardrailit + pituusohjaus | 0.5 pv | Faithfulness +5–10% |
| P3 | Token-efektiivisyys (MMR, cache) | 1 pv | −20–35% tokenit/kysymys |

## 🚀 Pika-voitot (Quick Wins)
- Poista ”...” ground truth -teksteistä ja lisää chunk-viitteet jokaiselle testille (1 työpäivä).
- Aja semanttinen deduplikointi (threshold 0.88) ja korvaa poistuneet uudentyyppisillä, numeerisilla tai disambiguation-kysymyksillä.
- Nosta 3-chunk -osuus täsmälleen 25%:iin ja lisää vähintään 8 uutta aidosti 4–5 chunkin monihyppyistä kysymystä.
- Lisää 10 ”harhautus”-tapausta (läheiset mutta virheelliset kontekstit) context_precisionin mittaamiseksi.
- Ota käyttöön cross-encoder-rerankkaus (bge-reranker-v2-m3) heti: tyypillisesti nopein parannus kontekstin relevanssiin.

## 🔬 A/B-testaussuunnitelma
- Koeasetelma
  - A (baseline): nykyinen retriever + ilman rerankkausta.
  - B (parannettu): hybrid (BM25+dense) + cross-encoder-rerankkaus + uudet testit (dedup + hard-negatives).
- Otoskoko ja stratifiointi
  - 200–300 kysymystä, stratifioitu kysymystyypin (short/reason/synth) ja chunk-määrän (1–5) mukaan.
- Mitattavat metriikat (RAGAS)
  - answer_relevancy (tavoite ≥ 0.90)
  - faithfulness (tavoite ≥ 0.85)
  - context_precision (tavoite ≥ 0.70)
  - context_recall (tavoite ≥ 0.80)
- Pysäytyskriteerit
  - B voittaa, jos kaikkien metriikoiden mediaani paranee ja vähintään kahdessa (precision/faithfulness) ero > +5%-yks.
- Koodiluonnos (ragas-arvio):
```python
# pip install ragas datasets
from ragas import evaluate
from ragas.metrics import answer_relevancy, faithfulness, context_precision, context_recall
from datasets import Dataset

def to_ds(rows):
    # rows: list of dict: {"question","answer","contexts","ground_truth"}
    return Dataset.from_list(rows)

ds_A = to_ds(rows_A)  # baseline vastaukset + kontekstit
ds_B = to_ds(rows_B)  # parannetun pipelinen vastaukset + kontekstit

metrics = [answer_relevancy, faithfulness, context_precision, context_recall]
report_A = evaluate(ds_A, metrics=metrics)
report_B = evaluate(ds_B, metrics=metrics)

print("A:", report_A)
print("B:", report_B)
```

## 📊 Monitorointi ja jatkuva parantaminen
- Päivittäinen regressiotesti: ajetaan 50–100 satunnaista testiä (stratifioitu).
- Aikasarjaseuranta: tallenna metriikat (faithfulness, ctx_precision/recall, answer_relevancy), tokenit/kysymys, kesto/kysymys.
- Hälytykset: jos faithfulness < 0.80 tai context_precision laskee >10% viikon keskiarvosta → Slack-hälytys.
- Drift-seuranta: dokumenttivektorien jakauman muutos (cosine center shift), kysymysten embedding-jakauma.
- Koodiluonnos (Prometheus-metriikat):
```python
# pip install prometheus_client
from prometheus_client import Gauge, push_to_gateway

g_faith = Gauge('ragas_faithfulness', 'RAGAS faithfulness score')
g_prec = Gauge('ragas_context_precision', 'RAGAS context precision')
g_recl = Gauge('ragas_context_recall', 'RAGAS context recall')
g_relv = Gauge('ragas_answer_relevancy', 'RAGAS answer relevancy')

def push_metrics(r):
    g_faith.set(r["faithfulness"])
    g_prec.set(r["context_precision"])
    g_recl.set(r["context_recall"])
    g_relv.set(r["answer_relevancy"])
    push_to_gateway('http://prometheus-pushgateway:9091', job='rag_eval', registry=None)
```

## 📝 Yhteenveto
- Nykytila
  - Testigenerointi on kustannustehokasta ja jakaumat osuvat tavoitteisiin, mutta testien laatu (duplikaatit, katkaistut ground truthit, vähäinen monihyppyisyys) heikentää evaluoinnin realistisuutta.
- Pääongelma
  - RAGAS-mittaus todennäköisesti yliarvioi suorituskyvyn, koska testit eivät sisällä riittävästi vaikeita, harhauttavia tai usean lähteen yhdistelyä vaativia tapauksia.
- Ratkaisu
  - P1: Deduplikointi, täydet ground truthit viitteineen, hard-negatives.
  - P1: Hybrid retrieval + cross-encoder-rerankkaus.
  - P2: Parempi chunkkaus ja generointipromptin sääntöjen tiukennus (monihyppy, numerot, disambiguation).
  - P3: Guardrailit vastausvaiheeseen ja token-efektiivisyyden parannukset.
- Odotettu tulos
  - Faithfulness +10–30%, context_precision +10–25%, context_recall +5–15%. Mittausten erottelu kasvaa ja tuotannon signaali vastaa paremmin evaluointia.
- Seuraavat askeleet
  - Päivä 1–2: Deduplikointi + GT-korjaukset + hard-negatives, lisää 8–12 monihyppyistä kysymystä.
  - Päivä 2–3: Ota käyttöön hybrid retrieval + reranker; tee A/B-mittaus.
  - Päivä 4: Säädä chunkkaus ja generointipromptti; aja regressiosetti; julkaise monitorointi ja hälytykset.