import os
import asyncio
from lightrag import LightRAG, QueryParam
from lightrag.llm.watsonx import watsonx_complete, watsonx_embed
from lightrag.utils import EmbeddingFunc
from lightrag.kg.shared_storage import initialize_pipeline_status
from lightrag.utils import setup_logger

# Lataa ympäristömuuttujat
from dotenv import load_dotenv
load_dotenv()

# Määritä lokitus
setup_logger("lightrag", level="INFO")

WORKING_DIR = os.getenv("WORKING_DIR", "./rag_storage_watsonx")
EMBEDDING_DIM = int(os.getenv("EMBEDDING_DIMENSION", "384"))

async def initialize_rag():
    """Alusta LightRAG WatsonX-konfiguraatiolla"""
    rag = LightRAG(
        working_dir=WORKING_DIR,
        llm_model_func=watsonx_complete,
        embedding_func=EmbeddingFunc(
            embedding_dim=EMBEDDING_DIM,
            max_token_size=8192,
            func=watsonx_embed
        )
    )
    
    await rag.initialize_storages()
    await initialize_pipeline_status()
    return rag

async def main():
    # Alusta RAG
    rag = await initialize_rag()
    
    # Indeksoi dokumentteja
    with open("./example_data.txt", "r") as f:
        text = f.read()
        await rag.ainsert(text)
    
    # Kyselyt eri modeissa
    modes = ["naive", "local", "global", "hybrid"]
    
    for mode in modes:
        print(f"\n{'='*20} Query mode: {mode} {'='*20}")
        response = await rag.aquery(
            "What are the main themes?",
            param=QueryParam(mode=mode)
        )
        print(response)

if __name__ == "__main__":
    asyncio.run(main())