#!/usr/bin/env python3
"""
RAGAS Test Runner - Yksinkertainen skripti RAGAS-testien ajamiseen
Käyttö: python run_ragas_test.py

HUOM: Voit asettaa API-avaimen suoraan koodissa tai komentorivillä!

Tapa 1 - Aseta API-avain suoraan tässä koodissa (turvallisin tapa kehityksessä):
"""

# ============================================================================
# ASETUKSET - Muokkaa näitä arvoja tarpeen mukaan
# ============================================================================

# OpenAI API-avain (aseta tähän oma avaimesi)
OPENAI_API_KEY = "..."


# LightRAG API asetukset
LIGHTRAG_ENDPOINT = "http://localhost:9622"
# JWT Bearer token (pitkä eyJhbG... alkava token)
LIGHTRAG_JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc2OTc1ODA1MCwicm9sZSI6InVzZXIiLCJtZXRhZGF0YSI6eyJhdXRoX21vZGUiOiJlbmFibGVkIn19.5DhRVY4mCM7w494PLiFsSn70u_M4yLYUx6oux8CPsGc"
# X-API-Key (lyhyempi avain)
LIGHTRAG_API_KEY = "your-secure-api-key-here-marko"

# Testitiedosto
# TEST_FILE = "nano_2advanced_testcases_aligned.json"

TEST_FILE = "Res_TestCases_20260130_055813.json"

# LLM ja Embedding mallit (valinnainen)
LLM_MODEL = "gpt-4o-mini"
EMBEDDING_MODEL = "text-embedding-3-large"

# Custom endpointit (valinnainen, jos käytät omia API:ja)
CUSTOM_LLM_HOST = None  # Esim: "http://localhost:8000/v1"
CUSTOM_EMBEDDING_HOST = None  # Esim: "http://localhost:8001/v1"

# Hakuasetukset
TOP_K = 10
QUERY_MODES = ["mix"]  # Oletus: vain mix mode. Vaihtoehdot: naive, local, global, hybrid, mix

# ============================================================================
# Älä muokkaa tästä alaspäin, ellei tiedä mitä teet
# ============================================================================

"""
Tapa 2 - Käytä komentoriviparametreja:
    python run_ragas_test.py --apikey sk-your-key --testfile my_tests.json

Tapa 3 - Käytä ympäristömuuttujia:
    export OPENAI_API_KEY=sk-your-key
    python run_ragas_test.py
"""

import os
import sys
import json
import requests
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Any

# Tarkista että ragas on asennettu
try:
    from ragas import evaluate
    from ragas.metrics import (
        faithfulness,
        answer_relevancy,
        context_recall,
        context_precision,
    )
    from datasets import Dataset
except ImportError as e:
    print("❌ Virhe: Tarvittavia kirjastoja puuttuu!")
    print("Asenna komennolla: pip install ragas datasets langfuse")
    print(f"Puuttuva kirjasto: {e}")
    sys.exit(1)

# Tarkista että langchain_openai on asennettu (tarvitaan RAGAS:lle)
try:
    from langchain_openai import ChatOpenAI, OpenAIEmbeddings
except ImportError:
    print("❌ Virhe: langchain_openai puuttuu!")
    print("Asenna komennolla: pip install langchain-openai")
    sys.exit(1)


# Token-hinnat (USD per 1M tokenia) - päivitetty 2024
TOKEN_PRICES = {
    "gpt-4o-mini": {"input": 0.150, "output": 0.600},
    "gpt-4o": {"input": 2.50, "output": 10.00},
    "gpt-4-turbo": {"input": 10.00, "output": 30.00},
    "gpt-3.5-turbo": {"input": 0.50, "output": 1.50},
    "text-embedding-3-small": {"input": 0.020, "output": 0.0},
    "text-embedding-3-large": {"input": 0.130, "output": 0.0},
    "text-embedding-ada-002": {"input": 0.100, "output": 0.0},
}


class RAGASTestRunner:
    """RAGAS-testien ajaja"""
    
    def __init__(
        self,
        test_file: str = "nano_testcases.json",
        rag_endpoint: str = "http://localhost:9621",
        rag_jwt_token: str = None,
        rag_api_key: str = None,
        openai_api_key: str = None,
        llm_model: str = None,
        embedding_model: str = None,
        llm_host: str = None,
        embedding_host: str = None,
        top_k: int = None,
        query_modes: list = None,
    ):
        self.test_file = test_file
        self.rag_endpoint = rag_endpoint
        
        # LightRAG autentikointi (JWT token ja API key)
        self.rag_jwt_token = rag_jwt_token or os.getenv("LIGHTRAG_JWT_TOKEN")
        self.rag_api_key = rag_api_key or os.getenv("LIGHTRAG_API_KEY")
        
        # OpenAI API-avain: ensin parametri, sitten ympäristömuuttuja
        self.api_key = openai_api_key or os.getenv("EVAL_LLM_BINDING_API_KEY") or os.getenv("OPENAI_API_KEY")
        
        # Mallit: ensin parametri, sitten ympäristömuuttuja, sitten oletus
        self.llm_model = llm_model or os.getenv("EVAL_LLM_MODEL", "gpt-4o-mini")
        self.embedding_model = embedding_model or os.getenv("EVAL_EMBEDDING_MODEL", "text-embedding-3-large")
        
        # Hostit: ensin parametri, sitten ympäristömuuttuja
        self.llm_host = llm_host or os.getenv("EVAL_LLM_BINDING_HOST")
        self.embedding_host = embedding_host or os.getenv("EVAL_EMBEDDING_BINDING_HOST") or self.llm_host
        
        # Top-K: ensin parametri, sitten ympäristömuuttuja, sitten oletus
        self.top_k = top_k if top_k is not None else int(os.getenv("EVAL_QUERY_TOP_K", "10"))
        
        # Query modes: ensin parametri, sitten koodi, sitten ympäristömuuttuja
        if query_modes:
            self.query_modes = query_modes if isinstance(query_modes, list) else [query_modes]
        elif 'QUERY_MODES' in globals():
            self.query_modes = QUERY_MODES if isinstance(QUERY_MODES, list) else [QUERY_MODES]
        else:
            env_mode = os.getenv("LIGHTRAG_QUERY_MODE", "mix")
            self.query_modes = [env_mode]
        
        # Tarkista API-avain
        if not self.api_key:
            print("❌ Virhe: API-avainta ei löydy!")
            print("Aseta OPENAI_API_KEY tai EVAL_LLM_BINDING_API_KEY ympäristömuuttuja")
            print("Esim: export OPENAI_API_KEY=sk-your-key-here")
            sys.exit(1)
        
        # Tuloskansio
        self.results_dir = Path("ragas_results")
        self.results_dir.mkdir(exist_ok=True)
        
        # Seuranta-muuttujat
        self.total_tokens = {"input": 0, "output": 0}
        self.start_time = None
        self.end_time = None
        
        print("=" * 70)
        print("🔍 RAGAS Test Runner - Asetukset")
        print("=" * 70)
        print(f"📁 Testitiedosto:        {self.test_file}")
        print(f"🌐 RAG Endpoint:         {self.rag_endpoint}")
        print(f"🔐 RAG JWT Token:        {'✓ Asetettu' if self.rag_jwt_token else '✗ Ei asetettu'}")
        print(f"🔑 RAG API Key:          {'✓ Asetettu' if self.rag_api_key else '✗ Ei asetettu'}")
        print(f"🔍 Query Modes:          {', '.join(self.query_modes)} ({len(self.query_modes)} modea)")
        print(f"🤖 LLM Malli:            {self.llm_model}")
        print(f"📊 Embedding Malli:      {self.embedding_model}")
        print(f"🔑 OpenAI API Key:       {'✓ Asetettu' if self.api_key else '✗ Puuttuu'}")
        print(f"📈 Top-K:                {self.top_k}")
        if self.llm_host:
            print(f"🔗 Custom LLM Host:      {self.llm_host}")
        if self.embedding_host and self.embedding_host != self.llm_host:
            print(f"🔗 Custom Embed Host:    {self.embedding_host}")
        print("=" * 70)
        print()
    
    def load_test_cases(self) -> List[Dict[str, Any]]:
        """Lataa testitapaukset JSON-tiedostosta"""
        # Etsi tiedosto useista paikoista
        search_paths = [
            self.test_file,
            os.path.join(os.getcwd(), self.test_file),
            os.path.join(os.path.dirname(os.path.abspath(__file__)), self.test_file),
        ]
        
        found_file = None
        for path in search_paths:
            if os.path.isfile(path):
                found_file = path
                break
        
        if not found_file:
            print(f"❌ Virhe: Tiedostoa {self.test_file} ei löydy!")
            print(f"\nEtsitty seuraavista paikoista:")
            for path in search_paths:
                print(f"  - {path}")
            print(f"\nLuo tiedosto tai määritä oikea polku parametrilla --testfile")
            sys.exit(1)
        
        try:
            with open(found_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            test_cases = data.get("test_cases", [])
            
            if not test_cases:
                print(f"❌ Virhe: Ei testitapauksia löydetty tiedostosta {found_file}")
                print("Tiedoston tulee sisältää 'test_cases' lista")
                sys.exit(1)
            
            print(f"✅ Ladattu {len(test_cases)} testitapausta tiedostosta {found_file}")
            return test_cases
            
        except json.JSONDecodeError as e:
            print(f"❌ Virhe: JSON-tiedoston parsinta epäonnistui: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Virhe tiedostoa lukiessa: {e}")
            sys.exit(1)
    
    def query_lightrag(self, question: str, query_mode: str) -> Dict[str, Any]:
        """Kysy LightRAG API:lta"""
        
        # Kokeillaan ensin JWT + API Key
        if self.rag_jwt_token and self.rag_api_key:
            result = self._try_query_with_auth(
                question,
                query_mode,
                jwt_token=self.rag_jwt_token, 
                api_key=self.rag_api_key,
                attempt_name="JWT + API Key"
            )
            if result:
                return result
        
        # Kokeillaan pelkkä API Key
        if self.rag_api_key:
            result = self._try_query_with_auth(
                question,
                query_mode,
                api_key=self.rag_api_key,
                attempt_name="Pelkkä API Key"
            )
            if result:
                return result
        
        # Kokeillaan pelkkä JWT
        if self.rag_jwt_token:
            result = self._try_query_with_auth(
                question,
                query_mode,
                jwt_token=self.rag_jwt_token,
                attempt_name="Pelkkä JWT"
            )
            if result:
                return result
        
        # Kokeillaan ilman autentikointia
        result = self._try_query_with_auth(
            question,
            query_mode,
            attempt_name="Ilman autentikointia"
        )
        if result:
            return result
        
        # Kaikki yritykset epäonnistuivat
        print(f"\n❌ Kaikki autentikointiyritykset epäonnistuivat!")
        print(f"\nRatkaisuehdotukset:")
        print(f"1. Hanki UUSI JWT token LightRAG:sta (vanha on vanhentunut)")
        print(f"2. Tarkista että API-avain on oikein")
        print(f"3. Testaa curl-komennolla että autentikointi toimii")
        sys.exit(1)
    
    def _try_query_with_auth(self, question: str, query_mode: str, jwt_token: str = None, api_key: str = None, attempt_name: str = "Unknown") -> Dict[str, Any]:
        """Yritä tehdä kysely tietyllä autentikoinnilla"""
        try:
            headers = {
                "accept": "application/json",
                "Content-Type": "application/json"
            }
            
            if jwt_token:
                headers["Authorization"] = f"Bearer {jwt_token}"
            
            if api_key:
                headers["X-API-Key"] = api_key
            
            response = requests.post(
                f"{self.rag_endpoint}/query",
                json={
                    "query": question,
                    "mode": query_mode,
                    "top_k": self.top_k,
                    "only_need_context": False,
                    "only_need_prompt": False,
                    "include_references": True,
                    "include_chunk_content": True,
                    "stream": False,
                },
                headers=headers,
                timeout=60
            )
            
            if response.status_code == 200:
                return response.json()
            
            if response.status_code == 401:
                print(f"⚠️  {attempt_name} epäonnistui: Autentikointi epäonnistui")
            else:
                print(f"⚠️  {attempt_name} epäonnistui: HTTP {response.status_code}")
            
            return None
            
        except requests.exceptions.RequestException as e:
            print(f"⚠️  {attempt_name} epäonnistui: {e}")
            return None
    
    def prepare_dataset(self, test_cases: List[Dict[str, Any]], query_mode: str) -> Dataset:
        """Valmistele dataset RAGAS:lle"""
        print(f"\n🔄 Haetaan vastauksia LightRAG:lta (mode: {query_mode})...")
        
        questions = []
        answers = []
        contexts = []
        ground_truths = []
        
        for i, test_case in enumerate(test_cases, 1):
            question = test_case.get("question", "")
            ground_truth = test_case.get("ground_truth", "")
            
            print(f"  {i}/{len(test_cases)}: {question[:60]}...")
            
            result = self.query_lightrag(question, query_mode)
            answer = result.get("response", "") if isinstance(result, dict) else ""
            
            # Käsittele contexts
            raw_contexts = result.get("references", []) if isinstance(result, dict) else []
            
            processed_contexts = []
            if raw_contexts:
                for ctx in raw_contexts:
                    text = None
                    
                    if isinstance(ctx, str):
                        text = ctx.strip()
                    elif isinstance(ctx, dict):
                        chunk_content = ctx.get('chunk_content')
                        content = ctx.get('content')
                        
                        if isinstance(content, list):
                            text = '\n\n'.join([str(c) for c in content if c])
                        elif chunk_content:
                            text = chunk_content
                        elif content:
                            text = content
                        else:
                            text = (ctx.get('text') or 
                                   ctx.get('page_content') or 
                                   ctx.get('chunk') or 
                                   ctx.get('source_text'))
                        
                        if not text or (isinstance(text, str) and not text.strip()):
                            ref_id = ctx.get('reference_id', 'unknown')
                            file_path = ctx.get('file_path', 'unknown')
                            text = f"Reference {ref_id} from {file_path}"
                    else:
                        text = str(ctx).strip()
                    
                    if text and isinstance(text, str) and text.strip() and text != "None":
                        processed_contexts.append(text.strip())
            
            if not processed_contexts:
                processed_contexts = ["No relevant context found for this query"]
            
            processed_contexts = [str(ctx) if not isinstance(ctx, str) else ctx for ctx in processed_contexts]
            
            questions.append(question)
            answers.append(answer)
            contexts.append(processed_contexts)
            ground_truths.append(ground_truth)
        
        dataset = Dataset.from_dict({
            "question": questions,
            "answer": answers,
            "contexts": contexts,
            "ground_truth": ground_truths,
        })
        
        print(f"✅ Dataset valmis: {len(dataset)} testitapausta")
        
        return dataset
    
    def run_evaluation(self, dataset: Dataset) -> Dict[str, Any]:
        """Aja RAGAS-evaluointi"""
        print("\n🚀 Aloitetaan RAGAS-evaluointi...")
        print("⏳ Tämä voi kestää muutaman minuutin...")
        
        # Luo LLM ja Embeddings
        llm_kwargs = {
            "model": self.llm_model,
            "api_key": self.api_key,
            "temperature": 0,
        }
        if self.llm_host:
            llm_kwargs["base_url"] = self.llm_host
        
        embedding_kwargs = {
            "model": self.embedding_model,
            "api_key": self.api_key,
        }
        if self.embedding_host:
            embedding_kwargs["base_url"] = self.embedding_host
        
        llm = ChatOpenAI(**llm_kwargs)
        embeddings = OpenAIEmbeddings(**embedding_kwargs)
        
        # Aja evaluointi
        try:
            result = evaluate(
                dataset,
                metrics=[
                    faithfulness,
                    answer_relevancy,
                    context_recall,
                    context_precision,
                ],
                llm=llm,
                embeddings=embeddings,
            )
            return result
            
        except Exception as e:
            print(f"❌ Virhe evaluoinnissa: {e}")
            print("\nMahdollisia syitä:")
            print("1. API rate limiting")
            print("2. Väärä API-avain tai endpoint")
            print("3. LightRAG API ei vastaa")
            raise
    
    def estimate_tokens_and_cost(self, dataset: Dataset, result: Dict[str, Any]) -> Dict[str, Any]:
        """Arvioi käytetyt tokenit ja kustannukset"""
        
        # Arvio: keskimäärin tokenien määrä
        # Input: kysymys + context + ground truth + RAGAS prompt overhead
        # Output: vastaus + RAGAS evaluointi vastaukset
        
        total_input_tokens = 0
        total_output_tokens = 0
        
        for i in range(len(dataset)):
            # Karkea arvio: 1 sana ≈ 1.3 tokenia englannissa, 1.5 suomessa
            question_tokens = len(dataset[i]['question'].split()) * 1.5
            answer_tokens = len(dataset[i]['answer'].split()) * 1.5
            ground_truth_tokens = len(dataset[i]['ground_truth'].split()) * 1.5
            
            # Kontekstit
            context_tokens = 0
            for ctx in dataset[i]['contexts']:
                context_tokens += len(ctx.split()) * 1.5
            
            # RAGAS käyttää LLM:ää jokaiselle metriikalle (4 metriikkaa)
            # Jokaiselle metriikalle: kysymys + vastaus + context + prompt
            metrics_count = 4
            
            # Input per metriikka
            input_per_metric = question_tokens + answer_tokens + context_tokens + 200  # +200 prompt overhead
            total_input_tokens += input_per_metric * metrics_count
            
            # Output per metriikka (RAGAS palauttaa arvioinnin, noin 100-200 tokenia per metriikka)
            output_per_metric = 150
            total_output_tokens += output_per_metric * metrics_count
        
        # Lisää embedding tokenit (embeddings käytetään answer_relevancy:ssä)
        # Arvio: jokaiselle kysymykselle embedataan kysymys ja vastaus
        embedding_tokens = 0
        for i in range(len(dataset)):
            question_tokens = len(dataset[i]['question'].split()) * 1.5
            answer_tokens = len(dataset[i]['answer'].split()) * 1.5
            embedding_tokens += (question_tokens + answer_tokens)
        
        # Laske kustannukset
        llm_price = TOKEN_PRICES.get(self.llm_model, {"input": 0, "output": 0})
        embedding_price = TOKEN_PRICES.get(self.embedding_model, {"input": 0, "output": 0})
        
        llm_input_cost = (total_input_tokens / 1_000_000) * llm_price["input"]
        llm_output_cost = (total_output_tokens / 1_000_000) * llm_price["output"]
        embedding_cost = (embedding_tokens / 1_000_000) * embedding_price["input"]
        
        total_cost = llm_input_cost + llm_output_cost + embedding_cost
        
        return {
            "total_input_tokens": int(total_input_tokens),
            "total_output_tokens": int(total_output_tokens),
            "total_embedding_tokens": int(embedding_tokens),
            "total_tokens": int(total_input_tokens + total_output_tokens + embedding_tokens),
            "llm_input_cost": llm_input_cost,
            "llm_output_cost": llm_output_cost,
            "embedding_cost": embedding_cost,
            "total_cost": total_cost,
        }
    
    def save_results(self, result: Dict[str, Any], dataset: Dataset, query_mode: str, duration: float, cost_info: Dict[str, Any]):
        """Tallenna tulokset"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Tallenna JSON
        json_file = self.results_dir / f"results_{query_mode}_{timestamp}.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            result_dict = {
                "timestamp": timestamp,
                "query_mode": query_mode,
                "duration_seconds": duration,
                "duration_formatted": str(timedelta(seconds=int(duration))),
                "cost_estimate": cost_info,
                "metrics": {k: float(v) for k, v in result.items() if k != "per_question"},
                "test_cases": []
            }
            
            for i in range(len(dataset)):
                test_result = {
                    "question": dataset[i]["question"],
                    "answer": dataset[i]["answer"],
                    "ground_truth": dataset[i]["ground_truth"],
                    "contexts": dataset[i]["contexts"],
                }
                if "per_question" in result:
                    for metric in ["faithfulness", "answer_relevancy", "context_recall", "context_precision"]:
                        if metric in result["per_question"]:
                            test_result[metric] = float(result["per_question"][metric][i])
                
                result_dict["test_cases"].append(test_result)
            
            json.dump(result_dict, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Tulokset tallennettu:")
        print(f"   📄 JSON: {json_file}")
        
        # Tallenna CSV
        try:
            csv_file = self.results_dir / f"Res_FinalReport_{query_mode}_{timestamp}.csv"
            result_df = result.to_pandas()
            result_df.to_csv(csv_file, index=False)
            print(f"   📊 CSV:  {csv_file}")
        except:
            pass
        
        # Tallenna Markdown-raportti
        md_file = self.results_dir / f"Res_FinalReport_results_{query_mode}_{timestamp}.md"
        self._save_markdown_report(md_file, result, dataset, query_mode, timestamp, duration, cost_info)
        print(f"   📝 Markdown: {md_file}")
    
    def _save_markdown_report(self, filepath: Path, result: Dict[str, Any], dataset: Dataset, 
                              query_mode: str, timestamp: str, duration: float, cost_info: Dict[str, Any]):
        """Luo yksityiskohtainen Markdown-raportti testituloksista"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            # Otsikko ja metatiedot
            f.write(f"# RAGAS Evaluointiraportti\n\n")
            f.write(f"**Aikaleima:** {timestamp}\n\n")
            f.write(f"**Query Mode:** `{query_mode}`\n\n")
            f.write(f"**Testitapausten määrä:** {len(dataset)}\n\n")
            
            # Testin kesto ja kustannukset
            duration_str = str(timedelta(seconds=int(duration)))
            f.write(f"**Testin kesto:** {duration_str} ({duration:.1f}s)\n\n")
            
            f.write(f"**Token-käyttö (arvio):**\n")
            f.write(f"- Input tokens: {cost_info['total_input_tokens']:,}\n")
            f.write(f"- Output tokens: {cost_info['total_output_tokens']:,}\n")
            f.write(f"- Embedding tokens: {cost_info['total_embedding_tokens']:,}\n")
            f.write(f"- **Yhteensä: {cost_info['total_tokens']:,} tokenia**\n\n")
            
            f.write(f"**Kustannusarvio:**\n")
            f.write(f"- LLM Input: ${cost_info['llm_input_cost']:.4f}\n")
            f.write(f"- LLM Output: ${cost_info['llm_output_cost']:.4f}\n")
            f.write(f"- Embeddings: ${cost_info['embedding_cost']:.4f}\n")
            f.write(f"- **Yhteensä: ${cost_info['total_cost']:.4f}**\n\n")
            
            f.write(f"---\n\n")
            
            # Kokonaistulokset
            f.write(f"## 📊 Kokonaistulokset\n\n")
            
            metrics = {
                "faithfulness": "Totuudenmukaisuus",
                "answer_relevancy": "Vastauksen relevanssi",
                "context_recall": "Kontekstin kattavuus",
                "context_precision": "Kontekstin tarkkuus",
            }
            
            f.write(f"| Metriikka | Tulos | Status |\n")
            f.write(f"|-----------|-------|--------|\n")
            
            for metric_key, metric_name in metrics.items():
                if metric_key in result:
                    score = result[metric_key]
                    status = "✅ Erinomainen" if score >= 0.8 else "⚠️ Hyvä" if score >= 0.6 else "❌ Heikko"
                    f.write(f"| {metric_name} | {score:.4f} | {status} |\n")
            
            # Keskiarvo
            avg_score = sum(result.get(k, 0) for k in metrics.keys()) / len(metrics)
            status = "✅ Erinomainen" if avg_score >= 0.8 else "⚠️ Hyvä" if avg_score >= 0.6 else "❌ Heikko"
            f.write(f"| **RAGAS Score (Keskiarvo)** | **{avg_score:.4f}** | **{status}** |\n\n")
            
            # Tulkinnat
            f.write(f"### Tulkinnat\n\n")
            f.write(f"- ✅ **0.80-1.00:** Erinomainen (Tuotantovalmis)\n")
            f.write(f"- ⚠️ **0.60-0.80:** Hyvä (Parannettavaa)\n")
            f.write(f"- ❌ **0.00-0.60:** Heikko (Vaatii optimointia)\n\n")
            f.write(f"---\n\n")
            
            # Yksittäiset testitapaukset
            f.write(f"## 🔍 Yksittäiset Testitapaukset\n\n")
            
            for i in range(len(dataset)):
                f.write(f"### Test Case #{i+1}\n\n")
                
                # Kysymys
                f.write(f"**Kysymys:**\n\n")
                f.write(f"{dataset[i]['question']}\n\n")
                
                # Ground Truth
                f.write(f"**Ground Truth (Odotettu vastaus):**\n\n")
                f.write(f"{dataset[i]['ground_truth']}\n\n")
                
                # Saatu vastaus
                f.write(f"**Saatu vastaus (RAG):**\n\n")
                f.write(f"{dataset[i]['answer']}\n\n")
                
                # Metriikat taulukkona
                f.write(f"**Metriikat:**\n\n")
                f.write(f"| Metriikka | Tulos | Status |\n")
                f.write(f"|-----------|-------|--------|\n")
                
                if "per_question" in result:
                    for metric_key, metric_name in metrics.items():
                        if metric_key in result["per_question"]:
                            score = float(result["per_question"][metric_key][i])
                            status = "✅" if score >= 0.8 else "⚠️" if score >= 0.6 else "❌"
                            f.write(f"| {metric_name} | {score:.4f} | {status} |\n")
                    
                    # Keskiarvo tälle kysymykselle
                    q_scores = [float(result["per_question"][k][i]) for k in metrics.keys() if k in result["per_question"]]
                    if q_scores:
                        q_avg = sum(q_scores) / len(q_scores)
                        status = "✅" if q_avg >= 0.8 else "⚠️" if q_avg >= 0.6 else "❌"
                        f.write(f"| **Keskiarvo** | **{q_avg:.4f}** | **{status}** |\n")
                
                f.write(f"\n")
                
                # Kontekstit
                f.write(f"<details>\n")
                f.write(f"<summary>📚 Haetut kontekstit (klikkaa nähdäksesi)</summary>\n\n")
                
                contexts = dataset[i]['contexts']
                for ctx_idx, ctx in enumerate(contexts, 1):
                    f.write(f"**Konteksti {ctx_idx}:**\n\n")
                    if len(ctx) > 500:
                        f.write(f"{ctx[:500]}...\n\n")
                    else:
                        f.write(f"{ctx}\n\n")
                
                f.write(f"</details>\n\n")
                f.write(f"---\n\n")
    
    def print_summary(self, result: Dict[str, Any], query_mode: str, duration: float, cost_info: Dict[str, Any]):
        """Tulosta yhteenveto"""
        print("\n" + "=" * 70)
        print(f"📊 RAGAS EVALUOINNIN TULOKSET - Mode: {query_mode.upper()}")
        print("=" * 70)
        
        metrics = {
            "faithfulness": "Totuudenmukaisuus",
            "answer_relevancy": "Vastauksen relevanssi",
            "context_recall": "Kontekstin kattavuus",
            "context_precision": "Kontekstin tarkkuus",
        }
        
        for metric_key, metric_name in metrics.items():
            if metric_key in result:
                score = result[metric_key]
                status = "✅" if score >= 0.8 else "⚠️" if score >= 0.6 else "❌"
                print(f"{status} {metric_name:25s}: {score:.4f}")
        
        # Keskiarvo
        avg_score = sum(result.get(k, 0) for k in metrics.keys()) / len(metrics)
        status = "✅" if avg_score >= 0.8 else "⚠️" if avg_score >= 0.6 else "❌"
        print("-" * 70)
        print(f"{status} {'RAGAS Score (Keskiarvo)':25s}: {avg_score:.4f}")
        print("=" * 70)
        
        # Testin tiedot
        duration_str = str(timedelta(seconds=int(duration)))
        print(f"\n⏱️  Testin kesto: {duration_str} ({duration:.1f}s)")
        print(f"🔢 Token-käyttö: {cost_info['total_tokens']:,} tokenia")
        print(f"💰 Kustannusarvio: ${cost_info['total_cost']:.4f}")
        
        print("\nTulkinnat:")
        print("✅ 0.80-1.00: Erinomainen (Tuotantovalmis)")
        print("⚠️  0.60-0.80: Hyvä (Parannettavaa)")
        print("❌ 0.00-0.60: Heikko (Vaatii optimointia)")
    
    def run(self):
        """Aja koko testi"""
        try:
            # Aloita ajanseuranta
            self.start_time = time.time()
            
            # Lataa testitapaukset
            test_cases = self.load_test_cases()
            
            # Aja testi (vain yhdelle modelle oletuksena)
            query_mode = self.query_modes[0]
            
            print(f"\n{'='*70}")
            print(f"🚀 Ajetaan RAGAS-testi (mode: {query_mode.upper()})")
            print(f"{'='*70}")
            
            # Valmistele dataset
            dataset = self.prepare_dataset(test_cases, query_mode)
            
            # Aja evaluointi
            result = self.run_evaluation(dataset)
            
            # Lopeta ajanseuranta
            self.end_time = time.time()
            duration = self.end_time - self.start_time
            
            # Arvioi kustannukset
            cost_info = self.estimate_tokens_and_cost(dataset, result)
            
            # Tallenna tulokset
            self.save_results(result, dataset, query_mode, duration, cost_info)
            
            # Tulosta yhteenveto
            self.print_summary(result, query_mode, duration, cost_info)
            
            print("\n✅ Testi suoritettu onnistuneesti!")
            
        except KeyboardInterrupt:
            print("\n\n⚠️  Testi keskeytetty käyttäjän toimesta")
            sys.exit(1)
        except Exception as e:
            print(f"\n❌ Virhe testin suorituksessa: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)


def main():
    """Pääohjelma"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Aja RAGAS-testi LightRAG:lle",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    parser.add_argument("-t", "--testfile", default=TEST_FILE, help=f"Testitiedosto (oletus: {TEST_FILE})")
    parser.add_argument("-e", "--endpoint", default=LIGHTRAG_ENDPOINT, help=f"LightRAG endpoint (oletus: {LIGHTRAG_ENDPOINT})")
    parser.add_argument("-j", "--jwt-token", default=LIGHTRAG_JWT_TOKEN if LIGHTRAG_JWT_TOKEN else None, help="JWT token")
    parser.add_argument("-r", "--rag-apikey", default=LIGHTRAG_API_KEY if LIGHTRAG_API_KEY else None, help="API key")
    parser.add_argument("-k", "--apikey", default=OPENAI_API_KEY if OPENAI_API_KEY else None, help="OpenAI API key")
    parser.add_argument("-m", "--model", default=LLM_MODEL if LLM_MODEL else None, help=f"LLM malli (oletus: {LLM_MODEL})")
    parser.add_argument("--embedding-model", default=EMBEDDING_MODEL if EMBEDDING_MODEL else None, help=f"Embedding malli (oletus: {EMBEDDING_MODEL})")
    parser.add_argument("--llm-host", default=CUSTOM_LLM_HOST, help="Custom LLM endpoint")
    parser.add_argument("--embedding-host", default=CUSTOM_EMBEDDING_HOST, help="Custom embedding endpoint")
    parser.add_argument("--top-k", type=int, default=TOP_K if TOP_K else None, help=f"Top-K (oletus: {TOP_K})")
    parser.add_argument("--query-mode", default=QUERY_MODES[0] if QUERY_MODES else "mix", 
                       choices=["naive", "local", "global", "hybrid", "mix"],
                       help="Query mode (oletus: mix)")
    
    args = parser.parse_args()
    
    runner = RAGASTestRunner(
        test_file=args.testfile,
        rag_endpoint=args.endpoint,
        rag_jwt_token=args.jwt_token,
        rag_api_key=args.rag_apikey,
        openai_api_key=args.apikey,
        llm_model=args.model,
        embedding_model=args.embedding_model,
        llm_host=args.llm_host,
        embedding_host=args.embedding_host,
        top_k=args.top_k,
        query_modes=[args.query_mode],
    )
    runner.run()


if __name__ == "__main__":
    main()