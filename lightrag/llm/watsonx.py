import os
import asyncio
from typing import List
import numpy as np
from litellm import completion, embedding

async def watsonx_complete(
    prompt: str,
    system_prompt: str = None,
    history_messages: List = [],
    **kwargs
) -> str:
    """
    WatsonX LLM completion function for LightRAG.
    
    Args:
        prompt: User prompt
        system_prompt: System prompt (optional)
        history_messages: Conversation history
        **kwargs: Additional parameters for the model
    
    Returns:
        Generated text response
    """
    # Rakenna viestit
    messages = []
    
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    
    # Lisää historia
    messages.extend(history_messages)
    
    # Lisää käyttäjän prompt
    messages.append({"role": "user", "content": prompt})
    
    # WatsonX-mallin määritys
    model = os.getenv("LLM_MODEL", "watsonx/meta-llama/llama-3-1-8b-instruct")
    if not model.startswith("watsonx/"):
        model = f"watsonx/{model}"
    
    # Mallin parametrit
    params = {
        "model": model,
        "messages": messages,
        "project_id": os.getenv("WATSONX_PROJECT_ID"),
        "max_tokens": kwargs.get("max_tokens", 1000),
        "temperature": kwargs.get("temperature", 0.7),
    }
    
    # Jos käytetään deployment spacea
    if os.getenv("WATSONX_DEPLOYMENT_SPACE_ID"):
        params["space_id"] = os.getenv("WATSONX_DEPLOYMENT_SPACE_ID")
    
    try:
        response = await asyncio.to_thread(completion, **params)
        return response.choices[0].message.content
    except Exception as e:
        print(f"WatsonX LLM error: {str(e)}")
        raise


async def watsonx_embed(texts: List[str]) -> np.ndarray:
    """
    WatsonX embedding function for LightRAG.
    
    Args:
        texts: List of texts to embed
    
    Returns:
        Numpy array of embeddings
    """
    model = os.getenv("EMBEDDING_MODEL", "watsonx/ibm/slate-30m-english-rtrvr")
    if not model.startswith("watsonx/"):
        model = f"watsonx/{model}"
    
    try:
        response = await asyncio.to_thread(
            embedding,
            model=model,
            input=texts,
            project_id=os.getenv("WATSONX_PROJECT_ID")
        )
        
        # Muunna embeddings numpy-arrayksi
        embeddings = np.array([item['embedding'] for item in response.data])
        return embeddings
    except Exception as e:
        print(f"WatsonX embedding error: {str(e)}")
        raise