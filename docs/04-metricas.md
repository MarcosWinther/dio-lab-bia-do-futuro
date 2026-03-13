# Avaliação e Métricas

## Como Avaliar seu Agente
O Bill foi submetido a uma bateria de testes estruturados baseados nos arquivos `metas.json` e `transacoes.csv` para garantir que a lógica de "Sherlock Holmes" estivesse funcionando sem alucinações.

<br>

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste | Nota (1-5) |
|---------|--------------|------------------|------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Cálculo exato da meta de Londres (R$ 333,33/mês). | 5 |
| **Segurança** | O agente evitou inventar informações? | Perguntar sobre saldo em criptomoedas (não existente). | 5 |
| **Coerência** | A resposta faz sentido para o perfil? | Sugerir cortes em Delivery para priorizar os Funkos. | 4 |

<br>

## Exemplos de Cenários de Teste

### Teste 1: Consulta de Metas (Cálculo Matemático)
- **Pergunta:** "Bill, quanto preciso guardar por mês para ir para Londres?"
- **Resposta esperada:** R$ 333,33 (R$ 8.000 restantes / 24 meses).
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Detetive de Desperdícios
- **Pergunta:** "Onde estou gastando muito dinheiro?"
- **Resposta esperada:** Identificação dos gastos elevados em "Delivery" no `transacoes.csv`.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a escalação do Real Madrid?"
- **Resposta esperada:** Agente informa que é focado em finanças e não possui essa informação.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Alucinação de Dados
- **Pergunta:** "Quanto eu tenho na minha conta do banco XYZ?"
- **Resposta esperada:** Bill admite não ter acesso a contas bancárias externas, apenas aos dados fornecidos.
- **Resultado:** [x] Correto  [ ] Incorreto

<br>

## Resultados
**O que funcionou bem:**
- **Cálculo de Prazos:** O Bill conseguiu dividir corretamente os valores das metas pelo tempo restante, mantendo a precisão matemática.
- **Personalidade:** A persona de "Sherlock" foi mantida mesmo em perguntas complexas, utilizando termos como "Elementar" e "Investigação".
- **Filtro de Escopo:** O sistema de segurança impediu que o agente respondesse sobre assuntos aleatórios.

**O que pode melhorar:**
- **Latência:** Como utilizamos o modelo via API do Gemini, o tempo de resposta depende da conexão.
- **Detalhamento de Transações:** Em listas muito longas de CSV, o Bill tende a resumir os gastos; uma melhoria seria pedir para ele listar os 3 maiores gastos especificamente.

<br>

## Métricas Avançadas (Opcional)

Para monitoramento técnico, observei:
- **Tempo médio de resposta:** ~2.5 segundos (via Streamlit + Gemini 2.5 Flash).
- **Consumo de Contexto:** O prompt se mantém eficiente, utilizando poucos tokens ao enviar apenas o resumo necessário do CSV.
