# Base de Conhecimento

## Dados Utilizados
O Bill utiliza os dados estruturados para realizar cálculos de prazos e identificar padrões de consumo.

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `metas.json` | JSON | Define os objetivos (Londres/Funkos), valores almejados e prazos. |
| `transacoes.csv` | CSV | Base para o motor de detecção de gastos excessivos e desperdícios. |

<br>

## Adaptações nos Dados
Os dados originais foram expandidos para incluir **prazos temporais específicos** (Timeframes).
- **Meta de Longo Prazo:** "Viagem para Londres" foi configurada para um horizonte de 24 meses.
- **Meta de Curto Prazo:** "Funkos e Action Figures" foi configurada para um horizonte de 4 meses.
Essa adaptação foi necessária para que o Bill pudesse calcular a **parcela mensal ideal** de economia.

<br>

## Estratégia de Integração

### Como os dados são carregados?
Os arquivos são carregados localmente via Python utilizando as bibliotecas `pandas` (para os CSVs) e `json`. O carregamento ocorre no início da execução do Streamlit, garantindo que o Bill sempre tenha as informações mais recentes antes de iniciar o chat.

[ex: Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt]

### Como os dados são usados no prompt?
Os dados são injetados diretamente no **System Prompt** (Context Injection). Transformamos os DataFrames e dicionários em strings formatadas que o Gemini processa como "memória de curto prazo". Isso permite que o modelo faça correlações diretas entre o saldo de uma meta e um gasto específico encontrado no histórico de transações.

<br>


## Exemplo de Contexto Montado
Abaixo, um exemplo de como o Bill "enxerga" os dados antes de responder ao usuário:

```text
CONTEXTO DO SISTEMA:
- Usuário focado em: Viagem para Londres (Faltam R$ 8.000 em 24 meses).
- Meta Secundária: Funkos (Faltam R$ 1.000 em 4 meses).

RESUMO DE TRANSAÇÕES RECENTES:
- Categoria 'Delivery': R$ 450,00 (Acima da média desejada).
- Categoria 'Assinaturas': R$ 120,00 (3 serviços ativos).

LÓGICA APLICADA:
Se o usuário reduzir 'Delivery' em 50%, a economia de R$ 225,00 cobre 90% da parcela mensal da meta de Funkos.
```
