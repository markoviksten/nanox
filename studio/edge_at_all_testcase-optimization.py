from openai import OpenAI
import os
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("LLM_BINDING_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("LLM_BINDING_API_KEY ei löydy .env-tiedostosta!")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
client = OpenAI()

# Etsi projektin juurihakemisto
script_dir = Path(__file__).parent.absolute()
project_root = script_dir
while project_root.name and not (project_root / "studio").exists():
    if project_root.parent == project_root:
        break
    project_root = project_root.parent
if not (project_root / "studio").exists():
    project_root = script_dir

# 1️⃣ Lue Edge et al. -evaluointiraportti
REPORT_PATH = project_root / "studio" / "testresults" / "er_naive_vs_mix_20260227_082045.md"
if not REPORT_PATH.exists():
    raise FileNotFoundError(f"Raporttitiedostoa ei löydy: {REPORT_PATH}")

with open(REPORT_PATH, "r", encoding="utf-8") as f:
    raportti = f.read()

print(f"📂 Projektin juuri: {project_root}")
print(f"📄 Luetaan raportti: {REPORT_PATH}")

# 2️⃣ System-prompt
SYSTEM_PROMPT = """
Olet RAG-asiantuntija ja arvioit Edge et al. (2024) -menetelmällä tehtyjä LLM-as-Judge parivertailutuloksia.

Arviointimenetelmä: Kaksi RAG-modea (Mode A ja Mode B) on vertailtu kysymyskohtaisesti kolmella dimensiolla:
- Kattavuus (Comprehensiveness): Kuinka kattavasti vastaus käsittelee kysymyksen kaikki osa-alueet
- Monipuolisuus (Diversity): Kuinka monipuolisesti näkökulmia ja tietoa esitetään
- Oivalluttavuus (Empowerment): Kuinka hyvin vastaus auttaa lukijaa ymmärtämään aihetta ja muodostamaan johtopäätöksiä

Pisteasteikko (0–100%):
- 80–100%: Erinomainen
- 60–79%: Hyvä
- 41–59%: Tyydyttävä
- 0–40%:  Heikko

VAATIMUKSET (PAKOLLISET):
- Vastaa SUOMEKSI
- Vastauksen TÄYTYY olla Markdown-muodossa
- Käytä TÄSMÄLLEEN alla määriteltyä rakennetta ja otsikoita
- Älä jätä mitään osioita pois
- Käytä taulukoita, emoji-merkintöjä ja teknisiä esimerkkejä
- Tee konkreettisia, toteutettavia optimointiehdotuksia
- Käytä koodiesimerkkejä Pythonilla

RAKENNE (ÄLÄ MUUTA OTSIKOITA):

# Edge et al. -evaluointitulosten Analyysi ja Optimointiehdotukset

## 📊 Yhteenveto tuloksista
- Kokonaisarvio: kumpi mode suoriutui paremmin ja millä marginaalilla
- Taulukko dimensioittain (dimensio, Mode A pisteet, Mode B pisteet, voittaja, selitys)
- Win rate -yhteenveto (kuinka monessa % kysymyksistä kumpikin voitti)

### Keskeiset havainnot
- ✅ Vahvuudet (kummankin moden parhaat puolet)
- ⚠️ Kehityskohteet (missä dimensioissa tai kysymystyypeissä on eniten parantamisen varaa)

## 🎯 Pääongelma
- Mikä dimensio tai kysymystyyppi tuotti heikoimmat pisteet
- Konkreettiset esimerkit heikoista kysymys-vastaus -pareista raportista
- Analyysi: johtuuko heikkous retrieval-vaiheesta, generation-vaiheesta vai molemmista

## 🔧 Optimointiehdotukset
- Priorisoidut toimenpiteet (P1, P2, P3)
- Jokaiselle: ongelma, ratkaisu, Python-koodiesimerkkejä LightRAG-asetuksista, arvioitu vaikutus pisteisiin

## 📈 Implementointijärjestys ja vaikutusarviot
- Taulukko: prioriteetti, toimenpide, työmäärä, arvioitu pisteparannus, kohde-dimensio

## 🚀 Pika-voitot (Quick Wins)
- Toimenpiteet jotka voi tehdä nopeasti ja joilla on iso vaikutus

## 🔬 Jatkovertailusuunnitelma
- Mitä modeja tai parametreja kannattaa seuraavaksi vertailla
- Ehdotettu kysymysjoukko tai kysymystyypit joihin tulisi panostaa
- Miten tuloksia tulisi seurata iteraatioiden välillä

## 📊 Monitorointi ja jatkuva parantaminen
- Miten seurata kehitystä eri evaluointikierrosten välillä
- Mitkä dimensiot ovat kriittisimpiä seurata

## 📝 Yhteenveto
- Nykytila (mode-vertailun tulos)
- Pääongelma
- Suositeltu ratkaisu
- Odotettu tulos optimoinnin jälkeen
- Seuraavat askeleet

ÄLÄ:
- muuta rakennetta
- tiivistä liikaa
- vastaa yleisellä tasolla
- sekoita RAGAS-terminologiaa (faithfulness, context_recall jne.) – käytä Edge et al. -dimensioita
"""

# 3️⃣ User-prompt
USER_PROMPT = """
Liitteenä Edge et al. (2024) -menetelmällä tehdyn LLM-as-Judge parivertailun tulokset.

Analysoi tulokset ja anna yksityiskohtaiset ehdotukset RAG-järjestelmän optimointitoimenpiteisiin.

Pisteasteikko:
- 80–100%: ✅ Erinomainen
- 60–79%:  ⚠️ Hyvä (parannettavaa)
- 41–59%:  ⚠️ Tyydyttävä (selkeitä puutteita)
- 0–40%:   ❌ Heikko (vaatii optimointia)

Kiinnitä erityistä huomiota:
1. Dimensioiden välisiin eroihin – missä on suurin kehityspotentiaali
2. Kysymyskohtaisiin tuloksiin – onko tiettyjä kysymystyyppejä joissa toistuu heikko suoriutuminen
3. Mode A vs Mode B -eroihin – mikä selittää voittavan moden paremmuuden
"""

# 4️⃣ OpenAI-kutsu
print("\n🚀 Lähetetään analyysi OpenAI:lle...")
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": f"{USER_PROMPT}\n\n---\n\n### Edge et al. -evaluointiraportti (lähde)\n\n{raportti}"
        }
    ],
)

# 5️⃣ Poimi vastaus
answer = response.choices[0].message.content

# 6️⃣ Kirjoita vastaus tiedostoon
output_dir = project_root / "studio" / "testresults"
output_dir.mkdir(parents=True, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
OUTPUT_FILE = output_dir / f"opt_{timestamp}.md"

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(answer)

print(f"\n✅ Edge et al. -analyysi luotu tiedostoon {OUTPUT_FILE}")
print(f"📊 Käytetty tokeneita: {response.usage.total_tokens}")
print(f"💰 Kustannus (arvio): ${(response.usage.total_tokens / 1_000_000) * 2.5:.4f}")