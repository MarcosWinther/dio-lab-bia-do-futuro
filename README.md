# 🕵️‍♂️ Bill: O Sherlock das Finanças

> **"Elementar, meu caro usuário: economizar é o primeiro passo para realizar."**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)](https://aistudio.google.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Dotenv](https://img.shields.io/badge/.env-ECD53F?style=for-the-badge&logo=dotenv&logoColor=black)](https://pypi.org/project/python-dotenv/)

O **Bill** é um mentor financeiro inteligente desenvolvido para o desafio de projeto da DIO. Ele atua como um "detetive de desperdícios", analisando transações reais e correlacionando-as diretamente com a velocidade de conquista dos seus sonhos.

<br>

## 🎯 Objetivo do Projeto

O Bill resolve a "cegueira do consumo" através de uma persona investigativa. O objetivo é transformar dados frios em insights motivadores:
1.  **Investigar:** Varre o histórico de `transacoes.csv` em busca de padrões de gastos (Delivery, Lazer, Assinaturas).
2.  **Correlacionar:** Conecta esses gastos com objetivos do `metas.json` (ex: Viagem para Londres ou Coleção de Funkos).
3.  **Quantificar:** Traduz a economia financeira em **tempo ganho**: *"Se você reduzir o delivery este mês, sua viagem acontece 20 dias antes"*.

<br>

## 🎓 Contexto Acadêmico

Este repositório é o resultado do projeto prático desenvolvido para o curso:
* **Curso:** *Desafio de Projeto Final — Construa seu Assistente Virtual com IA Generativa*
* **Instrutor:** [Venilton Falvo Jr](https://www.linkedin.com/in/falvojr/)
* **Plataforma:** [DIO (Digital Innovation One)](https://www.dio.me/)
* **Bootcamp Bradesco - GenAI & Dados**

<br>

## 🛠️ Ferramentas e Tecnologias

O projeto utiliza uma arquitetura modular moderna para garantir segurança e performance:

* **Python:** Linguagem base para processamento e lógica.
* **Google Gemini API:** O "cérebro" do agente, responsável pelo raciocínio e linguagem natural.
* **Streamlit:** Interface de usuário fluida e interativa.
* **Pandas:** Manipulação e análise eficiente da base de conhecimento (CSV).
* **Python-dotenv:** Gestão segura de credenciais e variáveis de ambiente.

<br>

## 📂 Estrutura do Repositório

```text
├── data/               # Base de conhecimento (JSON e CSV)
├── docs/               # Documentação das etapas do desafio (Persona, Métricas, etc.)
├── src/                # Código-fonte modularizado
│   ├── app.py          # Interface e visualização (Streamlit)
│   ├── agente.py       # Cérebro do Bill (Prompt Engineering e Lógica)
│   └── config.py       # Configurações de API e Segurança
├── .env                # Variáveis de ambiente (Chave de API)
├── .gitignore          # Proteção de arquivos e caches
└── requirements.txt    # Dependências do projeto
```

<br>

## 🚀 Como Executar

### 1. Preparação do Ambiente
Certifique-se de ter o Python 3.10 ou superior instalado. Clone este repositório:
```bash
git clone https://github.com/MarcosWinther/dio-lab-bia-do-futuro/
cd dio-lab-bia-do-futuro
```

### 2. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 3. Configuração da API Key
Crie um arquivo ``.env`` na raiz do projeto e insira sua chave do [Google AI Studio](https://aistudio.google.com/api-keys):
```
GOOGLE_API_KEY=sua_chave_aqui
```

### 4. Execução
```bash
streamlit run src/app.py
```

<br>

## 🧠 Inteligência e Segurança

O Bill foi configurado com estratégias avançadas de Anti-Alucinação:

* **Context Injection:** O agente só toma decisões baseadas nos dados injetados via System Prompt.
* **Filtro de Escopo:** O "Sherlock" ignora perguntas não financeiras, mantendo o foco na mentoria.
* **Segurança de Dados:** Uso de variáveis de ambiente para evitar a exposição de chaves sensíveis em repositórios públicos.

<br>

## 👨‍💻 Expert

<p>
    <img 
      align=left 
      margin=10 
      width=80 
      src="https://avatars.githubusercontent.com/u/44624583?v=4"
    />
    <p>&nbsp&nbsp&nbspMarcos Winther<br>
    &nbsp&nbsp&nbsp
    <a href="https://github.com/MarcosWinther">
    GitHub</a>&nbsp;|&nbsp;
    <a href="https://www.linkedin.com/in/marcoswinthersilva/">LinkedIn</a>
    </p>
</p>
<br/><br/>

---

⌨️ com 💜 por [Marcos Winther](https://github.com/MarcosWinther)

