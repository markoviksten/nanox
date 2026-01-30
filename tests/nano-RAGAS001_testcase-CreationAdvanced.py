import json
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
import time
from typing import List, Dict
from datetime import datetime, timedelta
import random

load_dotenv()
#laita oma tokenapikey
client = OpenAI(api_key="...")

# Token-hinnat (USD per 1M tokenia) - päivitetty 2024
TOKEN_PRICES = {
    "gpt-4o-mini": {"input": 0.150, "output": 0.600},
    "gpt-4o": {"input": 2.50, "output": 10.00},
    "gpt-4-turbo": {"input": 10.00, "output": 30.00},
    "gpt-3.5-turbo": {"input": 0.50, "output": 1.50},
}

# ============================================================================
# KONFIGURAATIO - Muokkaa näitä arvoja tarpeen mukaan
# ============================================================================

# ============================================================================
# AKTIIVINEN KONFIGURAATIO (muokkaa näitä):
# ============================================================================

# Chunk-määrä konfiguraatio (True/False)
ENABLE_SINGLE_CHUNK = True      # Yhden chunkin kysymykset
ENABLE_DUAL_CHUNK = True        # Kahden chunkin kysymykset
ENABLE_TRIPLE_CHUNK = True      # Kolmen chunkin kysymykset
ENABLE_QUAD_CHUNK = True        # Neljän chunkin kysymykset
ENABLE_QUINT_CHUNK = True       # Viiden chunkin kysymykset

# Kysymystyyppien konfiguraatio (True/False)
ENABLE_SHORT_FACTUAL = True     # Lyhyet täsmäkysymykset (faktat, määritelmät)
ENABLE_REASONING = True         # Päättelykysymykset (miksi, miten, syy-seuraus)
ENABLE_SYNTHESIS = True         # Yhdistelmäkysymykset (monimutkainen synteesi)
ENABLE_CONTACT_FACTUAL = True   # Yhteystietokysymykset (kuka, missä, yhteystiedot)

# Kysymysten jakauma (prosentit, yhteensä 100%)
# Määrittää kuinka monta prosenttia kysymyksistä on mitäkin tyyppiä
DISTRIBUTION = {
    "short_factual": 70,     # Lyhyitä täsmäkysymyksiä
    "reasoning": 4,         # Päättelykysymyksiä
    "synthesis": 2,         # Yhdistelmäkysymyksiä
    "contact_factual": 24,   # Yhteystietokysymyksiä
}

# Chunk-määrien jakauma (prosentit per chunk-tyyppi)
# Määrittää montako kysymystä luodaan kullekin chunk-määrälle
CHUNK_DISTRIBUTION = {
    "single": 60,    # kysymyksistä yhdestä chunkista
    "dual": 20,      # kahdesta chunkista
    "triple": 5,     # kolmesta chunkista
    "quad": 2,       # neljästä chunkista
    "quint": 1,      # viidestä chunkista
}

# Kokonaismäärä generoitavia kysymyksiä
TOTAL_QUESTIONS = 22

# Tiedostopolut
INPUT_FILE = "vdb_chunks.json"
# OUTPUT_FILE luodaan dynaamisesti timestampilla myöhemmin

# ============================================================================
# KÄYTTÖESIMERKIT (kommentoituna, voit kopioida ylös)
# ============================================================================

# ESIMERKKI 1: Vain lyhyet kysymykset yhdestä chunkista
# ------------------------------------------------------
# ENABLE_SINGLE_CHUNK = True
# ENABLE_DUAL_CHUNK = False
# ENABLE_TRIPLE_CHUNK = False
# ENABLE_QUAD_CHUNK = False
# ENABLE_QUINT_CHUNK = False
#
# ENABLE_SHORT_FACTUAL = True
# ENABLE_REASONING = False
# ENABLE_SYNTHESIS = False
# ENABLE_CONTACT_FACTUAL = False
#
# DISTRIBUTION = {
#     "short_factual": 100,
#     "reasoning": 0,
#     "synthesis": 0,
#     "contact_factual": 0,
# }
#
# CHUNK_DISTRIBUTION = {
#     "single": 100,
#     "dual": 0,
#     "triple": 0,
#     "quad": 0,
#     "quint": 0,
# }
#
# TOTAL_QUESTIONS = 30

# ESIMERKKI 2: Vain yhteystietokysymykset yhdestä chunkista
# ----------------------------------------------------------
# ENABLE_SINGLE_CHUNK = True
# ENABLE_DUAL_CHUNK = False
# ENABLE_TRIPLE_CHUNK = False
# ENABLE_QUAD_CHUNK = False
# ENABLE_QUINT_CHUNK = False
#
# ENABLE_SHORT_FACTUAL = False
# ENABLE_REASONING = False
# ENABLE_SYNTHESIS = False
# ENABLE_CONTACT_FACTUAL = True
#
# DISTRIBUTION = {
#     "short_factual": 0,
#     "reasoning": 0,
#     "synthesis": 0,
#     "contact_factual": 100,
# }
#
# CHUNK_DISTRIBUTION = {
#     "single": 100,
#     "dual": 0,
#     "triple": 0,
#     "quad": 0,
#     "quint": 0,
# }
#
# TOTAL_QUESTIONS = 20

# ESIMERKKI 3: Tasainen sekoitus kaikkea
# ---------------------------------------
# ENABLE_SINGLE_CHUNK = True
# ENABLE_DUAL_CHUNK = True
# ENABLE_TRIPLE_CHUNK = True
# ENABLE_QUAD_CHUNK = True
# ENABLE_QUINT_CHUNK = True
#
# ENABLE_SHORT_FACTUAL = True
# ENABLE_REASONING = True
# ENABLE_SYNTHESIS = True
# ENABLE_CONTACT_FACTUAL = True
#
# DISTRIBUTION = {
#     "short_factual": 25,
#     "reasoning": 25,
#     "synthesis": 25,
#     "contact_factual": 25,
# }
#
# CHUNK_DISTRIBUTION = {
#     "single": 20,
#     "dual": 20,
#     "triple": 20,
#     "quad": 20,
#     "quint": 20,
# }
#
# TOTAL_QUESTIONS = 100

# ============================================================================
# Älä muokkaa tästä alaspäin
# ============================================================================

# Yhtenäinen system prompt (vastaavuus tuotantopromptiin)
ALIGNED_SYSTEM_PROMPT = """You are an expert AI assistant specializing in synthesizing information from a provided knowledge base. Your primary function is to answer user queries accurately by ONLY using the information within the provided Context.

When generating test questions and ground truth answers for RAG evaluation:
- Carefully analyze the provided Context (one or more document chunks)
- Extract all relevant facts from the Context
- Synthesize a comprehensive, well-structured answer
- Use ONLY information explicitly stated in the Context
- Structure the response in clear paragraphs using Markdown formatting
- Answer in Finnish (same language as the query)
- DO NOT invent, assume, or infer information not in the Context"""

# Aseta työhakemisto
script_dir = Path(__file__).parent.absolute()
os.chdir(script_dir)

# Luo output-tiedostonimi timestampilla
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
OUTPUT_FILE = script_dir / f"Res_TestCases_{timestamp}.json"

print(f"Työhakemisto: {script_dir}")
print(f"Output tiedosto: {OUTPUT_FILE}\n")

print("="*80)
print("KONFIGUROITAVA TESTIKYSYMYSTEN GENEROINTI")
print("="*80)

# Tulosta konfiguraatio
print("\n📋 KONFIGURAATIO:")
print("-" * 80)
print(f"Chunk-määrät:")
print(f"  • Yksittäiset (1):  {'✓ Käytössä' if ENABLE_SINGLE_CHUNK else '✗ Ei käytössä'}")
print(f"  • Parit (2):        {'✓ Käytössä' if ENABLE_DUAL_CHUNK else '✗ Ei käytössä'}")
print(f"  • Kolmikot (3):     {'✓ Käytössä' if ENABLE_TRIPLE_CHUNK else '✗ Ei käytössä'}")
print(f"  • Nelikot (4):      {'✓ Käytössä' if ENABLE_QUAD_CHUNK else '✗ Ei käytössä'}")
print(f"  • Viisikot (5):     {'✓ Käytössä' if ENABLE_QUINT_CHUNK else '✗ Ei käytössä'}")
print(f"\nKysymystyypit:")
print(f"  • Lyhyet täsmäkysymykset:  {'✓ Käytössä' if ENABLE_SHORT_FACTUAL else '✗ Ei käytössä'}")
print(f"  • Päättelykysymykset:      {'✓ Käytössä' if ENABLE_REASONING else '✗ Ei käytössä'}")
print(f"  • Yhdistelmäkysymykset:    {'✓ Käytössä' if ENABLE_SYNTHESIS else '✗ Ei käytössä'}")
print(f"  • Yhteystietokysymykset:   {'✓ Käytössä' if ENABLE_CONTACT_FACTUAL else '✗ Ei käytössä'}")
print(f"\nJakauma (kysymystyypit):")
for qtype, pct in DISTRIBUTION.items():
    print(f"  • {qtype}: {pct}%")
print(f"\nJakauma (chunk-määrät):")
for ctype, pct in CHUNK_DISTRIBUTION.items():
    print(f"  • {ctype}: {pct}%")
print(f"\nYhteensä kysymyksiä: {TOTAL_QUESTIONS}")
print("="*80 + "\n")

# Lue data
json_path = Path('') / INPUT_FILE

try:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"✓ Ladattu {len(data['data'])} chunkkia\n")
except Exception as e:
    print(f"❌ Virhe: {e}")
    exit()

chunks = data['data']
all_test_cases = []

# ============================================================================
# CHUNK-RYHMIEN LUONTIFUNKTIOT
# ============================================================================

def create_chunk_groups(chunks: List[Dict], n: int, count: int = None) -> List[tuple]:
    """Luo n:n chunkin ryhmiä"""
    groups = []
    
    # Peräkkäiset ryhmät
    for i in range(len(chunks) - n + 1):
        groups.append(tuple(chunks[i:i+n]))
    
    # Rajaa määrää
    if count and len(groups) > count:
        groups = random.sample(groups, count)
    
    return groups

# ============================================================================
# KYSYMYSGENERAATTORIFUNKTIOT
# ============================================================================

def generate_question_prompt(chunks_content: str, num_chunks: int, question_type: str) -> str:
    """Generoi prompt kysymystyypille"""
    
    # Määritä chunk-vaatimus
    if num_chunks == 1:
        chunk_requirement = "tästä yhdestä osasta"
        chunk_desc = "YHDEN dokumentin osan"
    elif num_chunks == 2:
        chunk_requirement = "MOLEMMISTA osista"
        chunk_desc = "KAHDEN dokumentin osan"
    elif num_chunks == 3:
        chunk_requirement = "KAIKISTA KOLMESTA osasta"
        chunk_desc = "KOLMEN dokumentin osan"
    elif num_chunks == 4:
        chunk_requirement = "KAIKISTA NELJÄSTÄ osasta"
        chunk_desc = "NELJÄN dokumentin osan"
    elif num_chunks == 5:
        chunk_requirement = "KAIKISTA VIIDESTÄ osasta"
        chunk_desc = "VIIDEN dokumentin osan"
    else:
        chunk_requirement = f"KAIKISTA {num_chunks} osasta"
        chunk_desc = f"{num_chunks} dokumentin osan"
    
    # Määritä kysymystyyppi-spesifiset ohjeet
    if question_type == "short_factual":
        type_instructions = """
Luo LYHYT TÄSMÄKYSYMYS:
- Kysyy yhtä spesifistä faktaa, määritelmää tai tietoa
- Vastaus on lyhyt ja tarkka (1-3 lausetta)
- Tyypillisiä muotoja: "Mikä on X?", "Mitä tarkoittaa Y?", "Milloin Z?", "Kuinka monta A?"
- Ei vaadi laajaa päättelyä, vain faktan muistamista
"""
        num_questions = 2
        
    elif question_type == "reasoning":
        type_instructions = """
Luo PÄÄTTELYKYSYMYS:
- Vaatii syy-seuraussuhteiden ymmärtämistä
- Kysyy "miksi", "miten", "mistä johtuu"
- Vastaus selittää prosesseja, syitä tai seurauksia
- Vaatii dokumenttien ymmärtämistä, ei vain faktojen muistamista
- Vastaus 3-5 lausetta
"""
        num_questions = 2
        
    elif question_type == "synthesis":
        type_instructions = """
Luo MONIMUTKAINEN YHDISTELMÄKYSYMYS:
- Vaatii tiedon syntetisointia useista paikoista
- Kysyy kokonaisuuksista, vertailuista, tai monimutkaisista suhteista
- Tyypillisiä muotoja: "Miten X ja Y liittyvät toisiinsa?", "Vertaile A ja B", "Kuvaile prosessi kokonaisuutena"
- Vastaus on kattava ja yhdistää useita tietoja (4-8 lausetta)
"""
        num_questions = 1
        
    elif question_type == "contact_factual":
        type_instructions = """
Luo YHTEYSTIETOKYSYMYS:
- Kysyy henkilöiden, organisaatioiden, järjestelmien tai palveluiden yhteystietoja
- Tyypillisiä muotoja: 
  * "Kuka on X?" / "Kuka hoitaa Y:n?"
  * "Missä sijaitsee Z?" / "Mistä löytyy A?"
  * "Mikä on X:n osoite/URL/sähköposti/puhelinnumero?"
  * "Keneen otan yhteyttä kun...?"
  * "Missä on tietojärjestelmä/palvelu/toimipiste X?"
- Vastaus sisältää täsmälliset yhteystiedot (nimi, sijainti, osoite, URL, yhteystiedot jne.)
- EDELLYTYS: Luo tämä kysymys VAIN jos dokumentissa on:
  * Henkilönimiä ja rooleja/vastuualueita
  * Organisaatioiden tai yksiköiden nimiä ja sijainteja
  * Järjestelmien tai palveluiden nimiä ja osoitteita (URL, verkko-osoite)
  * Toimipisteiden tai tilojen nimiä ja sijainteja
  * Puhelinnumeroita, sähköposteja tai muita yhteystietoja
- Jos dokumentissa EI OLE mitään edellä mainittua, ÄLÄ LUO tätä kysymystä
- Vastaus 1-3 lausetta
"""
        num_questions = 2
    else:
        type_instructions = "Luo kysymys joka sopii annettuun kontekstiin."
        num_questions = 1
    
    prompt = f"""---Role---
You are an expert at creating test questions for RAG system evaluation that require synthesizing information from multiple document chunks.

---Goal---
Generate {num_questions} test question(s) and corresponding ground truth answer(s). Each question must require information from {chunk_desc}.

---Context---
{chunks_content}

---Instructions---

{type_instructions}

Step-by-Step for Question Generation:
1. Carefully analyze ALL {num_chunks} document chunk(s) in the Context
2. Identify information that is relevant for the question type
3. Create question(s) that REQUIRE information from {chunk_requirement}
4. Ensure the question matches the specified type (factual/reasoning/synthesis/contact_factual)

Step-by-Step for Ground Truth Generation:
1. Carefully determine what the question asks
2. Scrutinize the document chunk(s) and extract relevant facts
3. Weave extracted facts into a coherent, well-structured answer
4. Use ONLY information explicitly stated in the Context
5. DO NOT invent, assume, or infer any information not in the Context
6. Match answer length to question type

Content & Grounding for Ground Truth:
- Strictly adhere to provided Context; DO NOT introduce external information
- Integrate facts from all relevant chunks
- Use your knowledge ONLY to formulate fluent sentences, NOT to add facts
- The answer must demonstrate that the required chunks were necessary

Formatting & Language:
- Both questions and answers MUST be in Finnish
- Ground truth answers should use Markdown formatting when appropriate
- Structure should be clear and logical

Return ONLY a JSON object:
{{
  "questions": [
    {{
      "question": "Kysymys joka vaatii {chunk_requirement}?",
      "ground_truth": "Vastaus joka syntetisoi tiedon {chunk_requirement}...",
      "question_type": "{question_type}",
      "num_chunks": {num_chunks}
    }}
  ]
}}"""
    
    return prompt, num_questions

def generate_test_cases(chunks_group: tuple, question_type: str) -> tuple:
    """Generoi testikysymykset tietylle chunk-ryhmälle ja kysymystyypille
    
    Returns:
        tuple: (test_cases: List[Dict], tokens_used: Dict)
    """
    
    num_chunks = len(chunks_group)
    
    # Muodosta yhdistetty sisältö
    combined_content = ""
    for i, chunk in enumerate(chunks_group, 1):
        combined_content += f"CHUNK {i}:\n{chunk['content']}\n\n---\n\n"
    
    # Generoi prompt
    prompt, num_questions = generate_question_prompt(combined_content, num_chunks, question_type)
    
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[
                {"role": "system", "content": ALIGNED_SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            max_tokens=3500,
            temperature=0.8,
            response_format={"type": "json_object"}
        )
        
        # Hae token-käyttö
        tokens_used = {
            "input": response.usage.prompt_tokens,
            "output": response.usage.completion_tokens,
            "total": response.usage.total_tokens
        }
        
        response_text = response.choices[0].message.content
        questions_data = json.loads(response_text)
        questions_list = questions_data.get('questions', [])
        
        # Muunna test caseiksi
        test_cases = []
        for q in questions_list:
            test_case = {
                "question": q.get('question', ''),
                "ground_truth": q.get('ground_truth', ''),
                "project": "nano_rag_evaluation",
                "metadata": {
                    "question_type": question_type,
                    "num_chunks": num_chunks,
                }
            }
            test_cases.append(test_case)
        
        return test_cases, tokens_used
        
    except Exception as e:
        print(f"  ❌ Virhe generoinnissa: {e}")
        return [], {"input": 0, "output": 0, "total": 0}

# ============================================================================
# PÄÄOHJELMA - TESTIKYSYMYSTEN GENEROINTI
# ============================================================================

# Laske kuinka monta kysymystä per tyyppi
enabled_types = []
if ENABLE_SHORT_FACTUAL:
    enabled_types.append("short_factual")
if ENABLE_REASONING:
    enabled_types.append("reasoning")
if ENABLE_SYNTHESIS:
    enabled_types.append("synthesis")
if ENABLE_CONTACT_FACTUAL:
    enabled_types.append("contact_factual")

# Normalisoi jakauma (jos jokin tyyppi on disabloitu)
total_dist = sum(DISTRIBUTION[t] for t in enabled_types)
normalized_dist = {t: (DISTRIBUTION[t] / total_dist) for t in enabled_types}

# Laske kysymysmäärät per tyyppi
questions_per_type = {t: int(TOTAL_QUESTIONS * normalized_dist[t]) for t in enabled_types}

# Varmista että yhteensä on oikea määrä
diff = TOTAL_QUESTIONS - sum(questions_per_type.values())
if diff > 0 and enabled_types:
    questions_per_type[enabled_types[0]] += diff

print(f"📊 Kysymysmäärät per tyyppi:")
for qtype, count in questions_per_type.items():
    print(f"  • {qtype}: {count} kysymystä")
print()

# Laske chunk-määrät
enabled_chunks = []
if ENABLE_SINGLE_CHUNK:
    enabled_chunks.append(("single", 1))
if ENABLE_DUAL_CHUNK:
    enabled_chunks.append(("dual", 2))
if ENABLE_TRIPLE_CHUNK:
    enabled_chunks.append(("triple", 3))
if ENABLE_QUAD_CHUNK:
    enabled_chunks.append(("quad", 4))
if ENABLE_QUINT_CHUNK:
    enabled_chunks.append(("quint", 5))

# Normalisoi chunk-jakauma
total_chunk_dist = sum(CHUNK_DISTRIBUTION[name] for name, _ in enabled_chunks)
normalized_chunk_dist = {name: (CHUNK_DISTRIBUTION[name] / total_chunk_dist) for name, _ in enabled_chunks}

# Generoi kysymykset
print("="*80)
print("ALOITETAAN TESTIKYSYMYSTEN GENEROINTI")
print("="*80 + "\n")

start_time = time.time()
total_generated = 0
total_tokens = {"input": 0, "output": 0, "total": 0}

# Käy läpi jokainen kysymystyyppi
for question_type, type_count in questions_per_type.items():
    if type_count == 0:
        continue
    
    print(f"\n{'='*80}")
    print(f"Generoidaan {question_type.upper()} kysymyksiä ({type_count} kpl)")
    print(f"{'='*80}\n")
    
    # Jaa kysymykset chunk-määrien kesken
    for chunk_name, chunk_size in enabled_chunks:
        chunk_count = int(type_count * normalized_chunk_dist[chunk_name])
        
        if chunk_count == 0:
            continue
        
        print(f"  [{chunk_name}] {chunk_size}-chunk kysymyksiä: {chunk_count} kpl")
        
        # Luo chunk-ryhmät
        groups = create_chunk_groups(chunks, chunk_size, count=chunk_count * 2)  # Luo 2x määrä varalta
        
        generated_this_batch = 0
        for group in groups:
            if generated_this_batch >= chunk_count:
                break
            
            # Generoi kysymykset
            new_cases, tokens_used = generate_test_cases(group, question_type)
            
            # Päivitä token-laskurit
            total_tokens["input"] += tokens_used["input"]
            total_tokens["output"] += tokens_used["output"]
            total_tokens["total"] += tokens_used["total"]
            
            for case in new_cases:
                if generated_this_batch >= chunk_count:
                    break
                all_test_cases.append(case)
                generated_this_batch += 1
                total_generated += 1
            
            # Pieni viive API rate limitin takia
            time.sleep(0.5)
        
        print(f"    ✓ Luotu {generated_this_batch} kysymystä\n")

end_time = time.time()
duration = end_time - start_time

# Laske kustannukset
model_prices = TOKEN_PRICES.get("gpt-4o-mini", {"input": 0, "output": 0})
input_cost = (total_tokens["input"] / 1_000_000) * model_prices["input"]
output_cost = (total_tokens["output"] / 1_000_000) * model_prices["output"]
total_cost = input_cost + output_cost

# ============================================================================
# TALLENNUS
# ============================================================================

final_output = {
    "test_cases": all_test_cases,
    "metadata": {
        "total_questions": len(all_test_cases),
        "generation_time_seconds": duration,
        "generation_time_formatted": str(timedelta(seconds=int(duration))),
        "tokens_used": total_tokens,
        "cost_estimate": {
            "input_cost": input_cost,
            "output_cost": output_cost,
            "total_cost": total_cost,
            "model": "gpt-4o-mini"
        },
        "configuration": {
            "enable_single_chunk": ENABLE_SINGLE_CHUNK,
            "enable_dual_chunk": ENABLE_DUAL_CHUNK,
            "enable_triple_chunk": ENABLE_TRIPLE_CHUNK,
            "enable_quad_chunk": ENABLE_QUAD_CHUNK,
            "enable_quint_chunk": ENABLE_QUINT_CHUNK,
            "enable_short_factual": ENABLE_SHORT_FACTUAL,
            "enable_reasoning": ENABLE_REASONING,
            "enable_synthesis": ENABLE_SYNTHESIS,
            "enable_contact_factual": ENABLE_CONTACT_FACTUAL,
            "distribution": DISTRIBUTION,
            "chunk_distribution": CHUNK_DISTRIBUTION,
        }
    }
}

output_path = Path(OUTPUT_FILE).absolute()

print(f"\n{'='*80}")
print(f"TALLENNUS")
print(f"{'='*80}\n")

try:
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_output, f, ensure_ascii=False, indent=2)
    
    if output_path.exists():
        file_size = output_path.stat().st_size
        print(f"✓ TALLENNETTU ONNISTUNEESTI!")
        print(f"  Sijainti: {output_path}")
        print(f"  Koko: {file_size:,} tavua")
        print(f"  Kysymyksiä: {len(all_test_cases)}")
        print(f"  Generointi kesti: {duration:.1f}s")
        print(f"  Token-käyttö: {total_tokens['total']:,} tokenia")
        print(f"  Kustannusarvio: ${total_cost:.4f}\n")
        
        # Näytä jakauma
        print("📊 Generoitujen kysymysten jakauma:")
        
        # Per tyyppi
        type_counts = {}
        for tc in all_test_cases:
            qtype = tc.get('metadata', {}).get('question_type', 'unknown')
            type_counts[qtype] = type_counts.get(qtype, 0) + 1
        
        print("\n  Kysymystyypit:")
        for qtype, count in type_counts.items():
            pct = (count / len(all_test_cases)) * 100
            print(f"    • {qtype}: {count} kpl ({pct:.1f}%)")
        
        # Per chunk-määrä
        chunk_counts = {}
        for tc in all_test_cases:
            num_chunks = tc.get('metadata', {}).get('num_chunks', 0)
            chunk_counts[num_chunks] = chunk_counts.get(num_chunks, 0) + 1
        
        print("\n  Chunk-määrät:")
        for num, count in sorted(chunk_counts.items()):
            pct = (count / len(all_test_cases)) * 100
            print(f"    • {num}-chunk: {count} kpl ({pct:.1f}%)")
        
        # Näytä esimerkkejä
        print("\n📝 Esimerkkikysymyksiä (3 ensimmäistä):")
        for i, tc in enumerate(all_test_cases[:3], 1):
            qtype = tc.get('metadata', {}).get('question_type', 'unknown')
            num_chunks = tc.get('metadata', {}).get('num_chunks', 0)
            print(f"\n  [{i}] {qtype} ({num_chunks}-chunk)")
            print(f"      Q: {tc['question'][:100]}...")
            print(f"      A: {tc['ground_truth'][:100]}...")
        print()
    
except Exception as e:
    print(f"❌ Virhe tallennuksessa: {e}\n")

# ============================================================================
# MARKDOWN-RAPORTIN LUONTI
# ============================================================================

print(f"{'='*80}")
print(f"LUODAAN MARKDOWN-RAPORTTI")
print(f"{'='*80}\n")

# Käytä samaa timestampia kuin JSON-tiedostossa
md_filename = script_dir / f"NanoRagas_TestCases_{timestamp}_report.md"
md_path = Path(md_filename).absolute()

try:
    with open(md_filename, 'w', encoding='utf-8') as f:
        # Otsikko
        f.write(f"# Testikysymysten Generointiraportti\n\n")
        
        # Metatiedot
        report_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"**Luotu:** {report_timestamp}\n\n")
        f.write(f"**Input tiedosto:** `{INPUT_FILE}`\n\n")
        f.write(f"**Output tiedosto:** `{OUTPUT_FILE.name}`\n\n")
        f.write(f"---\n\n")
        
        # Yhteenveto
        f.write(f"## 📊 Yhteenveto\n\n")
        
        duration_str = str(timedelta(seconds=int(duration)))
        f.write(f"| Metriikka | Arvo |\n")
        f.write(f"|-----------|------|\n")
        f.write(f"| **Luotuja kysymyksiä** | {len(all_test_cases)} kpl |\n")
        f.write(f"| **Generointi kesti** | {duration_str} ({duration:.1f}s) |\n")
        f.write(f"| **Input tokens** | {total_tokens['input']:,} |\n")
        f.write(f"| **Output tokens** | {total_tokens['output']:,} |\n")
        f.write(f"| **Yhteensä tokens** | {total_tokens['total']:,} |\n")
        f.write(f"| **Input kustannus** | ${input_cost:.4f} |\n")
        f.write(f"| **Output kustannus** | ${output_cost:.4f} |\n")
        f.write(f"| **Kokonaiskustannus** | **${total_cost:.4f}** |\n")
        f.write(f"| **Käytetty malli** | gpt-4.1-nano |\n\n")
        
        f.write(f"---\n\n")
        
        # Konfiguraatio
        f.write(f"## ⚙️ Konfiguraatio\n\n")
        
        f.write(f"### Chunk-määrät\n\n")
        f.write(f"| Chunk-tyyppi | Käytössä | Tavoite % |\n")
        f.write(f"|--------------|----------|----------|\n")
        f.write(f"| Single (1) | {'✓' if ENABLE_SINGLE_CHUNK else '✗'} | {CHUNK_DISTRIBUTION.get('single', 0)}% |\n")
        f.write(f"| Dual (2) | {'✓' if ENABLE_DUAL_CHUNK else '✗'} | {CHUNK_DISTRIBUTION.get('dual', 0)}% |\n")
        f.write(f"| Triple (3) | {'✓' if ENABLE_TRIPLE_CHUNK else '✗'} | {CHUNK_DISTRIBUTION.get('triple', 0)}% |\n")
        f.write(f"| Quad (4) | {'✓' if ENABLE_QUAD_CHUNK else '✗'} | {CHUNK_DISTRIBUTION.get('quad', 0)}% |\n")
        f.write(f"| Quint (5) | {'✓' if ENABLE_QUINT_CHUNK else '✗'} | {CHUNK_DISTRIBUTION.get('quint', 0)}% |\n\n")
        
        f.write(f"### Kysymystyypit\n\n")
        f.write(f"| Kysymystyyppi | Käytössä | Tavoite % |\n")
        f.write(f"|---------------|----------|----------|\n")
        f.write(f"| Short Factual | {'✓' if ENABLE_SHORT_FACTUAL else '✗'} | {DISTRIBUTION.get('short_factual', 0)}% |\n")
        f.write(f"| Reasoning | {'✓' if ENABLE_REASONING else '✗'} | {DISTRIBUTION.get('reasoning', 0)}% |\n")
        f.write(f"| Synthesis | {'✓' if ENABLE_SYNTHESIS else '✗'} | {DISTRIBUTION.get('synthesis', 0)}% |\n")
        f.write(f"| Contact Factual | {'✓' if ENABLE_CONTACT_FACTUAL else '✗'} | {DISTRIBUTION.get('contact_factual', 0)}% |\n\n")
        
        f.write(f"---\n\n")
        
        # Toteutunut jakauma
        f.write(f"## 📈 Toteutunut Jakauma\n\n")
        
        # Kysymystyypit
        f.write(f"### Kysymystyypit\n\n")
        f.write(f"| Tyyppi | Määrä | Osuus |\n")
        f.write(f"|--------|-------|-------|\n")
        for qtype, count in type_counts.items():
            pct = (count / len(all_test_cases)) * 100
            f.write(f"| {qtype} | {count} | {pct:.1f}% |\n")
        f.write(f"\n")
        
        # Chunk-määrät
        f.write(f"### Chunk-määrät\n\n")
        f.write(f"| Chunk-määrä | Määrä | Osuus |\n")
        f.write(f"|-------------|-------|-------|\n")
        for num, count in sorted(chunk_counts.items()):
            pct = (count / len(all_test_cases)) * 100
            f.write(f"| {num}-chunk | {count} | {pct:.1f}% |\n")
        f.write(f"\n")
        
        f.write(f"---\n\n")
        
        # Testikysymykset taulukkona
        f.write(f"## 📝 Generoidut Testikysymykset\n\n")
        
        f.write(f"| # | Tyyppi | Chunkit | Kysymys | Ground Truth |\n")
        f.write(f"|---|--------|---------|---------|-------------|\n")
        
        for i, tc in enumerate(all_test_cases, 1):
            qtype = tc.get('metadata', {}).get('question_type', 'unknown')
            num_chunks = tc.get('metadata', {}).get('num_chunks', 0)
            question = tc['question'][:80] + "..." if len(tc['question']) > 80 else tc['question']
            answer = tc['ground_truth'][:80] + "..." if len(tc['ground_truth']) > 80 else tc['ground_truth']
            
            # Korvaa pipe-merkit jotta taulukko ei hajoa
            question = question.replace('|', '\\|')
            answer = answer.replace('|', '\\|')
            
            f.write(f"| {i} | {qtype} | {num_chunks} | {question} | {answer} |\n")
        
        f.write(f"\n")
        
        f.write(f"---\n\n")
        
        # Esimerkkejä kokonaisina
        f.write(f"## 🔍 Esimerkkejä (Ensimmäiset 5)\n\n")
        
        for i, tc in enumerate(all_test_cases[:5], 1):
            qtype = tc.get('metadata', {}).get('question_type', 'unknown')
            num_chunks = tc.get('metadata', {}).get('num_chunks', 0)
            
            f.write(f"### Esimerkki {i}: {qtype} ({num_chunks}-chunk)\n\n")
            f.write(f"**Kysymys:**\n\n")
            f.write(f"{tc['question']}\n\n")
            f.write(f"**Ground Truth:**\n\n")
            f.write(f"{tc['ground_truth']}\n\n")
            f.write(f"---\n\n")
    
    print(f"✓ Markdown-raportti luotu: {md_path}\n")
    
except Exception as e:
    print(f"❌ Virhe Markdown-raportin luonnissa: {e}\n")

# ============================================================================
# YHTEENVETO
# ============================================================================
print(f"{'='*80}")
print(f"YHTEENVETO")
print(f"{'='*80}")
print(f"Input: {len(chunks)} chunkkia")
print(f"Output: {len(all_test_cases)} test casea")
print(f"Generointi kesti: {duration:.1f}s")
print(f"Tiedosto: {output_path}")
print(f"{'='*80}\n")