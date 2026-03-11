import streamlit as st
import pandas as pd
import json
import google.generativeai as genai
import os
from dotenv import load_dotenv

# --- CARREGAR VARIÁVEIS DE AMBIENTE ---
load_dotenv() # Carrega o arquivo .env
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("Erro: Variável GOOGLE_API_KEY não encontrada. Verifique o arquivo .env")
    st.stop()

genai.configure(api_key=api_key)

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Bill: O Sherlock das Finanças", page_icon="🕵️‍♂️")

# --- CARREGAMENTO DE DADOS ---
def load_data():
    # Caminho ajustado pois o app.py está em /src
    with open('../data/metas.json', 'r', encoding='utf-8') as f:
        metas = json.load(f)
    transacoes = pd.read_csv('../data/transacoes.csv', encoding='utf-8')
    return metas, transacoes

try:
    metas, transacoes = load_data()
except FileNotFoundError:
    st.error("Erro: Certifique-se de que a pasta 'data' está no nível correto.")

# --- SYSTEM PROMPT ---
SYSTEM_PROMPT = f"""
Você é o Bill, um mentor financeiro inteligente e motivador, estilo Sherlock Holmes.
Sua missão: Identificar desperdícios e ajudar o usuário a bater metas.

DADOS REAIS DO USUÁRIO:
- Metas: {json.dumps(metas)}
- Resumo de Transações: {transacoes.to_string()}

REGRAS:
1. Sempre use os dados acima para responder.
2. Calcule prazos: Londres em 24 meses, Funkos em 4 meses.
3. Traduza economias em "tempo ganho" na meta.
4. Use linguagem simples e encorajadora.
"""

# --- INTERFACE ---
st.title("🕵️‍♂️ Bill: O Sherlock das Finanças")

# Sidebar com progresso real
st.sidebar.header("🎯 Seus Objetivos")
for m in metas:
    prog = m['valor_poupado'] / m['valor_almejado']
    st.sidebar.write(f"**{m['objetivo']}**")
    st.sidebar.progress(prog)

# --- CHAT COM GEMINI ---
if "chat_session" not in st.session_state:
    model = genai.GenerativeModel('gemini-2.5-flash')
    st.session_state.chat_session = model.start_chat(history=[])
    # Enviando o System Prompt como primeira instrução "invisível"
    st.session_state.chat_session.send_message(SYSTEM_PROMPT)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do usuário
if prompt := st.chat_input("Pergunte ao Bill..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Chamada real para a API do Google
        response = st.session_state.chat_session.send_message(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})