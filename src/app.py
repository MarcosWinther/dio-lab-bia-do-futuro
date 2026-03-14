import streamlit as st
import pandas as pd
import json
import os
from config import setup_env
from agente import get_system_prompt, iniciar_chat

# Configuração e API
genai = setup_env()

# Carregamento de Dados
def load_data():
    base_path = os.path.dirname(__file__)
    with open(os.path.join(base_path, '../data/metas.json'), 'r', encoding='utf-8') as f:
        metas = json.load(f)
    transacoes = pd.read_csv(os.path.join(base_path, '../data/transacoes.csv'))
    return metas, transacoes

metas, transacoes = load_data()

# Interface Streamlit
st.set_page_config(page_title="Bill: Sherlock Financeiro", page_icon="🕵️‍♂️")
st.title("🕵️‍♂️ Bill: O Sherlock das Finanças")

# Sidebar
st.sidebar.header("🎯 Metas")
for m in metas:
    st.sidebar.write(f"**{m['objetivo']}**")
    st.sidebar.progress(m['valor_poupado'] / m['valor_almejado'])

# Gerenciamento do Chat
if "chat_session" not in st.session_state:
    model = genai.GenerativeModel('gemini-2.5-flash')
    system_prompt = get_system_prompt(metas, transacoes)
    st.session_state.chat_session = iniciar_chat(model, system_prompt)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Pergunte ao Bill..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.session_state.chat_session.send_message(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})