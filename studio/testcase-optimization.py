from openai import OpenAI
import os
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# Lataa ympäristömuuttujat .env-tiedostosta
load_dotenv()

# OpenAI API-avain luetaan .env-tiedostosta
OPENAI_API_KEY = os.getenv("LLM_BINDING_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("LLM_BINDING_API_KEY ei löydy .env-tiedostosta!")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
client = OpenAI()

# Etsi projektin juurihakemisto
script_dir = Path(__file__).parent.absolute()
project_root = script_dir

# Etsi projektin juuri (jossa on studio-kansio)
while project_root.name and not (project_root / "studio").exists():
    if project_root.parent == project_root:
        break
    project_root = project_root.parent

# Jos ei löydy, käytä script_dir:iä
if not (project_root / "studio").exists():
    project_root = script_dir

# 1️⃣ Lue liitetiedosto projektin juuresta
REPORT_PATH = project_root / "studio" / "testresults" / "tr_mix_20260212_084731.md"

if not REPORT_PATH.exists():
    raise FileNotFoundError(f"Raporttitiedostoa ei löydy: {REPORT_PATH}")

with open(REPORT_PATH, "r", encoding="utf-8") as f:
    raportti = f.read()

print(f"📂 Projektin juuri: {project_root}")
print(f"📄 Luetaan raportti: {REPORT_PATH}")

# 2️⃣ System-prompt: lukitaan rakenne ja tyyli
SYSTEM_PROMPT = """
Olet RAG-asiantuntija ja arvioit RAGAS-testituloksia.

VAATIMUKSET (PAKOLLISET):
- Vastaa SUOMEKSI
- Vastauksen TÄYTYY olla Markdown-muodossa
- Käytä TÄSMÄLLEEN alla määriteltyä rakennetta ja otsikoita
- Älä jätä mitään osioita pois
- Käytä taulukoita, emoji-merkintöjä ja teknisiä esimerkkejä
- Tee konkreettisia, toteutettavia optimointiehdotuksia
- Käytä koodiesimerkkejä Pythonilla

RAKENNE (ÄLÄ MUUTA OTSIKOITA):

# RAGAS-testituloksien Analyysi ja Optimointiehdotukset

## 📊 Yhteenveto tuloksista
- Kokonaisarvio
- Taulukko metriikoista (tulos, tavoite, status)

### Keskeiset havainnot
- ✅ Vahvuudet
- ⚠️ Kehityskohteet

## 🎯 Pääongelma
- Yksityiskohtainen ongelman kuvaus
- Konkreettiset esimerkit

## 🔧 Optimointiehdotukset
- Priorisoidut toimenpiteet (P1, P2, P3)
- Jokaiselle: ongelma, ratkaisu, koodi, arvioitu vaikutus

## 📈 Implementointijärjestys ja vaikutusarviot
- Taulukko: prioriteetti, työmäärä, vaikutus

## 🚀 Pika-voitot (Quick Wins)

## 🔬 A/B-testaussuunnitelma

## 📊 Monitorointi ja jatkuva parantaminen

## 📝 Yhteenveto
- Nykytila
- Pääongelma
- Ratkaisu
- Odotettu tulos
- Seuraavat askeleet

ÄLÄ:
- muuta rakennetta
- tiivistä liikaa
- vastaa yleisellä tasolla
"""

# 3️⃣ User-prompt
USER_PROMPT = """
Liitteenä RAGAS testien tulokset.

Analysoi tulokset ja anna yksityiskohtaiset ehdotukset ratkaisun optimointitoimenpiteisiin.
Tavoitetasot on seuraavat:
✅ 0.80-1.00: Erinomainen (Tuotantovalmis)
⚠️  0.60-0.80: Hyvä (Parannettavaa)
❌ 0.00-0.60: Heikko (Vaatii optimointia)

"""

# 4️⃣ OpenAI-kutsu
print("\n🚀 Lähetetään analyysi OpenAI:lle...")
response = client.chat.completions.create(
    model="gpt-4o",  # tai "gpt-4o-mini" halvempaan versioon
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": f"{USER_PROMPT}\n\n---\n\n### RAGAS-testiraportti (lähde)\n\n{raportti}"
        }
    ],
)

# 5️⃣ Poimi vastaus
answer = response.choices[0].message.content

# 6️⃣ Luo output-hakemisto jos ei ole olemassa
output_dir = project_root / "studio" / "testresults"
output_dir.mkdir(parents=True, exist_ok=True)

# 7️⃣ Kirjoita vastaus tiedostoon
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
OUTPUT_FILE = output_dir / f"opt_{timestamp}.md"

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(answer)

print(f"\n✅ RAGAS-analyysi luotu tiedostoon {OUTPUT_FILE}")
print(f"📊 Käytetty tokeneita: {response.usage.total_tokens}")
print(f"💰 Kustannus (arvio): ${(response.usage.total_tokens / 1_000_000) * 2.5:.4f}")