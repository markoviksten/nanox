from openai import OpenAI
import os
from pathlib import Path
from datetime import datetime

# OpenAI API-avain (aseta tähän oma avaimesi)
OPENAI_API_KEY = "..."

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
client = OpenAI()

# 1️⃣ Lue liitetiedosto
BASE_DIR = Path(__file__).resolve().parent
REPORT_PATH = BASE_DIR / "Res_FinalReport_results_mix_20260130_062000.md"

with open(REPORT_PATH, "r", encoding="utf-8") as f:
    raportti = f.read()

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
"""

# 4️⃣ OpenAI-kutsu (KORJATTU)
response = client.chat.completions.create(
    model="gpt-5",  # tai "gpt-4o-mini" halvempaan versioon
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

# 5️⃣ Poimi vastaus (KORJATTU)
answer = response.choices[0].message.content

# 6️⃣ Kirjoita vastaus tiedostoon
# 6️⃣ Kirjoita vastaus tiedostoon
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
OUTPUT_FILE = BASE_DIR / f"Res_Optimization_{timestamp}.md"
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(answer)

print(f"✅ RAGAS-analyysi luotu tiedostoon {OUTPUT_FILE}")
print(f"📊 Käytetty tokeneita: {response.usage.total_tokens}")
print(f"💰 Kustannus (arvio): ${(response.usage.total_tokens / 1_000_000) * 2.5:.4f}")