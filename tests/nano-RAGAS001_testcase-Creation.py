import json
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
import time
from typing import List, Dict
import random

load_dotenv()

# Lisää token
client = OpenAI(api_key="...")


# Aseta työhakemisto skriptin kansioon
script_dir = Path(__file__).parent.absolute()
os.chdir(script_dir)
print(f"Työhakemisto: {script_dir}\n")

print("="*80)
print("ADVANCED TESTIKYSYMYSTEN GENEROINTI (MULTI-CHUNK GRAPH RAG EVALUATION)")
print("="*80)

# Lue data
json_path = Path('') / 'vdb_chunks.json'

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
# YHTENÄINEN SYSTEM PROMPT (vastaavuus tuotantopromptiin)
# ============================================================================

ALIGNED_SYSTEM_PROMPT = """You are an expert AI assistant specializing in synthesizing information from a provided knowledge base. Your primary function is to answer user queries accurately by ONLY using the information within the provided Context.

When generating ground truth answers for RAG evaluation:
- Carefully analyze the provided Context (multiple document chunks)
- Extract all relevant facts from the Context
- Synthesize a comprehensive, well-structured answer
- Use ONLY information explicitly stated in the Context
- Structure the response in clear paragraphs using Markdown formatting
- Answer in Finnish (same language as the query)
- DO NOT invent, assume, or infer information not in the Context"""

# ============================================================================
# CHUNK-RYHMIEN LUONTIFUNKTIOT
# ============================================================================

def create_chunk_triplets(chunks: List[Dict], num_triplets: int = None) -> List[tuple]:
    """Luo kolmen chunkin ryhmiä monimutkaisempiin testeihin"""
    triplets = []
    
    # Peräkkäiset kolmikot
    for i in range(len(chunks) - 2):
        triplets.append((chunks[i], chunks[i+1], chunks[i+2]))
    
    # Rajaa määrää
    if num_triplets and len(triplets) > num_triplets:
        triplets = random.sample(triplets, num_triplets)
    
    return triplets

def create_chunk_quadruplets(chunks: List[Dict], num_quadruplets: int = None) -> List[tuple]:
    """Luo neljän chunkin ryhmiä erittäin monimutkaisiin testeihin"""
    quadruplets = []
    
    # Peräkkäiset nelikot
    for i in range(len(chunks) - 3):
        quadruplets.append((chunks[i], chunks[i+1], chunks[i+2], chunks[i+3]))
    
    # Rajaa määrää
    if num_quadruplets and len(quadruplets) > num_quadruplets:
        quadruplets = random.sample(quadruplets, num_quadruplets)
    
    return quadruplets

def create_chunk_quintuplets(chunks: List[Dict], num_quintuplets: int = None) -> List[tuple]:
    """Luo viiden chunkin ryhmiä maksimaalisen monimutkaisiin testeihin"""
    quintuplets = []
    
    # Peräkkäiset viisikot
    for i in range(len(chunks) - 4):
        quintuplets.append((chunks[i], chunks[i+1], chunks[i+2], chunks[i+3], chunks[i+4]))
    
    # Rajaa määrää
    if num_quintuplets and len(quintuplets) > num_quintuplets:
        quintuplets = random.sample(quintuplets, num_quintuplets)
    
    return quintuplets

# ============================================================================
# YHTENÄINEN KYSYMYSTEN JA GROUND TRUTH GENEROINTI
# ============================================================================

def generate_test_case_with_aligned_prompt(combined_content: str, num_chunks: int, num_questions: int = 1):
    """Generoi testikysymykset käyttäen tuotantopromptia vastaavaa logiikkaa"""
    
    # Määritä kysymystyyppi chunkkien määrän mukaan
    if num_chunks == 3:
        complexity_desc = "KOLMEN dokumentin osan yhdistämistä"
        chunk_requirement = "KAIKISTA KOLMESTA osasta"
    elif num_chunks == 4:
        complexity_desc = "NELJÄN dokumentin osan yhdistämistä"
        chunk_requirement = "KAIKISTA NELJÄSTÄ osasta"
    elif num_chunks == 5:
        complexity_desc = "VIIDEN dokumentin osan yhdistämistä"
        chunk_requirement = "KAIKISTA VIIDESTÄ osasta"
    else:
        complexity_desc = f"{num_chunks} dokumentin osan yhdistämistä"
        chunk_requirement = f"KAIKISTA {num_chunks} osasta"
    
    prompt = f"""---Role---
You are an expert at creating test questions for RAG system evaluation that require synthesizing information from multiple document chunks.

---Goal---
Generate {num_questions} test question(s) and corresponding ground truth answer(s). Each question must require information from ALL {num_chunks} document chunks provided in the Context.

---Context---
{combined_content}

---Instructions---

Step-by-Step for Question Generation:
1. Carefully analyze ALL {num_chunks} document chunks in the Context
2. Identify information that spans across ALL chunks (processes, relationships, hierarchies, etc.)
3. Create question(s) that REQUIRE synthesizing information from ALL {num_chunks} chunks
4. Questions should test one of these patterns:
   - MULTI-STEP PROCESS: Process continues across all chunks
   - COMPLEX RELATIONSHIP: Information complements across chunks
   - HOLISTIC UNDERSTANDING: Complete picture requires all chunks
   - HIERARCHY: e.g., general rule → specification → exception
   - BROAD CONTEXT: Requires understanding wide context

Step-by-Step for Ground Truth Generation:
1. Carefully determine what the question asks
2. Scrutinize ALL {num_chunks} document chunks and extract relevant facts
3. Weave extracted facts into a coherent, well-structured answer
4. Use ONLY information explicitly stated in the Context
5. DO NOT invent, assume, or infer any information not in the Context
6. If complete answer cannot be formed from Context, note what's missing

Content & Grounding for Ground Truth:
- Strictly adhere to provided Context; DO NOT introduce external information
- Integrate facts from ALL {num_chunks} chunks where relevant
- Use your knowledge ONLY to formulate fluent sentences, NOT to add facts
- The answer must demonstrate that ALL {num_chunks} chunks were necessary

Formatting & Language:
- Both questions and answers MUST be in Finnish
- Ground truth answers should use Markdown formatting (headings, bold, bullets)
- Present answers in multiple paragraphs when appropriate
- Structure should be clear and logical

AVOID:
- Questions answerable with fewer chunks
- Simple listing of information
- Adding information not in the Context

Return ONLY a JSON object:
{{
  "questions": [
    {{
      "question": "Kysymys joka vaatii {chunk_requirement}?",
      "ground_truth": "Kattava vastaus joka syntetisoi tiedon {chunk_requirement}..."
    }}
  ]
}}"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system", 
                    "content": ALIGNED_SYSTEM_PROMPT
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            max_tokens=3500,
            temperature=0.8,
            response_format={"type": "json_object"}
        )
        
        response_text = response.choices[0].message.content
        questions_data = json.loads(response_text)
        return questions_data.get('questions', [])
        
    except Exception as e:
        print(f"  ❌ Virhe generoinnissa: {e}")
        return []

# ============================================================================
# 3-CHUNK TEST CASES
# ============================================================================
print("\n" + "="*80)
print("GENEROIDAAN 3-CHUNK TEST CASEJA")
print("="*80 + "\n")

chunk_triplets = create_chunk_triplets(chunks, num_triplets=15)

for idx, (chunk1, chunk2, chunk3) in enumerate(chunk_triplets, 1):
    print(f"[{idx}/{len(chunk_triplets)}] 3-chunk triplet...")
    
    combined_content = f"""CHUNK 1:
{chunk1['content']}

---

CHUNK 2:
{chunk2['content']}

---

CHUNK 3:
{chunk3['content']}"""
    
    questions_list = generate_test_case_with_aligned_prompt(
        combined_content=combined_content,
        num_chunks=3,
        num_questions=2
    )
    
    for q in questions_list:
        test_case = {
            "question": q.get('question', ''),
            "ground_truth": q.get('ground_truth', ''),
            "project": "nano_rag_evaluation"
        }
        all_test_cases.append(test_case)
    
    print(f"  ✓ Luotu {len(questions_list)} kysymystä")
    time.sleep(0.5)

# ============================================================================
# 4-CHUNK TEST CASES
# ============================================================================
print("\n" + "="*80)
print("GENEROIDAAN 4-CHUNK TEST CASEJA")
print("="*80 + "\n")

chunk_quadruplets = create_chunk_quadruplets(chunks, num_quadruplets=10)

for idx, (chunk1, chunk2, chunk3, chunk4) in enumerate(chunk_quadruplets, 1):
    print(f"[{idx}/{len(chunk_quadruplets)}] 4-chunk quadruplet...")
    
    combined_content = f"""CHUNK 1:
{chunk1['content']}

---

CHUNK 2:
{chunk2['content']}

---

CHUNK 3:
{chunk3['content']}

---

CHUNK 4:
{chunk4['content']}"""
    
    questions_list = generate_test_case_with_aligned_prompt(
        combined_content=combined_content,
        num_chunks=4,
        num_questions=1
    )
    
    for q in questions_list:
        test_case = {
            "question": q.get('question', ''),
            "ground_truth": q.get('ground_truth', ''),
            "project": "nano_rag_evaluation"
        }
        all_test_cases.append(test_case)
    
    print(f"  ✓ Luotu {len(questions_list)} kysymystä")
    time.sleep(0.5)

# ============================================================================
# 5-CHUNK TEST CASES
# ============================================================================
print("\n" + "="*80)
print("GENEROIDAAN 5-CHUNK TEST CASEJA")
print("="*80 + "\n")

chunk_quintuplets = create_chunk_quintuplets(chunks, num_quintuplets=5)

for idx, (chunk1, chunk2, chunk3, chunk4, chunk5) in enumerate(chunk_quintuplets, 1):
    print(f"[{idx}/{len(chunk_quintuplets)}] 5-chunk quintuplet...")
    
    combined_content = f"""CHUNK 1:
{chunk1['content']}

---

CHUNK 2:
{chunk2['content']}

---

CHUNK 3:
{chunk3['content']}

---

CHUNK 4:
{chunk4['content']}

---

CHUNK 5:
{chunk5['content']}"""
    
    questions_list = generate_test_case_with_aligned_prompt(
        combined_content=combined_content,
        num_chunks=5,
        num_questions=1
    )
    
    for q in questions_list:
        test_case = {
            "question": q.get('question', ''),
            "ground_truth": q.get('ground_truth', ''),
            "project": "nano_rag_evaluation"
        }
        all_test_cases.append(test_case)
    
    print(f"  ✓ Luotu {len(questions_list)} kysymystä")
    time.sleep(0.5)

# ============================================================================
# TALLENNUS
# ============================================================================
final_output = {
    "test_cases": all_test_cases
}

output_file = 'nano_2advanced_testcases_aligned.json'
output_path = Path(output_file).absolute()

print(f"\n{'='*80}")
print(f"TALLENNUS")
print(f"{'='*80}\n")

try:
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(final_output, f, ensure_ascii=False, indent=2)
    
    if output_path.exists():
        file_size = output_path.stat().st_size
        print(f"✓ TALLENNETTU ONNISTUNEESTI!")
        print(f"  Sijainti: {output_path}")
        print(f"  Koko: {file_size:,} tavua\n")
        
        # Näytä ensimmäiset 2 esimerkkiä
        if len(all_test_cases) > 0:
            print("Ensimmäiset test caset:")
            print(json.dumps(all_test_cases[:2], ensure_ascii=False, indent=2))
            print()
    
except Exception as e:
    print(f"❌ Virhe tallennuksessa: {e}\n")

# ============================================================================
# YHTEENVETO
# ============================================================================
print(f"{'='*80}")
print(f"YHTEENVETO")
print(f"{'='*80}")
print(f"Chunkkeja yhteensä: {len(chunks)}")
print(f"Test cases yhteensä: {len(all_test_cases)}")
print(f"{'='*80}\n")

print(f"✓ Tiedosto tallennettu: {output_path}\n")