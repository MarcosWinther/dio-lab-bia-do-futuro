import os
from dotenv import load_dotenv
import google.generativeai as genai

def setup_env():
    # Caminho para o .env que está na raiz (um nível acima de src)
    load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        raise ValueError("GOOGLE_API_KEY não encontrada no arquivo .env")
    
    genai.configure(api_key=api_key)
    return genai