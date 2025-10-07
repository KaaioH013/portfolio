import pandas as pd          # pip install pandas
import streamlit as st  # pip install streamlit
import matplotlib.pyplot as plt # <--- ADICIONE ESTA LINHA  # pip install matplotlib
import seaborn as sns         # <--- ADICIONE ESTA LINHA # pip install seaborn

# --- CONFIGURAÇÃO DA PÁGINA ---
# st.set_page_config() deve ser o primeiro comando Streamlit a ser executado.
st.set_page_config(
    page_title="Dashboard de Vendas de Games",
    page_icon="🎮", # Você pode usar emojis como ícones!
    layout="wide"     # 'wide' faz a página usar toda a largura da tela.
)

# --- TÍTULO E INTRODUÇÃO ---
st.title("Vendas de Games 🎮")
st.write("Análise das vendas globais de mais de 16 mil jogos.") # st.write() escreve texto na tela

# --- CARREGANDO OS DADOS ---
# Carregamos o dataframe que já conhecemos.
df_games = pd.read_csv("dia_07_projeto_vendas_games/datasets/vgsales.csv")

def plotar_vendas_agrupadas(dataframe, coluna_categoria, coluna_valor):
    """
    Esta função recebe um DataFrame e os nomes de duas colunas.
    Ela agrupa os dados pela coluna de categoria, soma os valores
    e plota o resultado em um gráfico de barras.
    """
    print(f"\n--- Análise de Vendas por: {coluna_categoria} ---")

    # 1. Agrupamento, soma e ordenação (a mesma lógica de ontem, agora genérica)
    analise = dataframe.groupby(coluna_categoria)[coluna_valor].sum().sort_values(ascending=False)

    # 2. Exibição do resultado no terminal
    print(analise.head()) # .head() para não poluir o terminal se a lista for muito grande

    # 3. Criação do gráfico com títulos e rótulos dinâmicos
    plt.figure(figsize=(12, 6))
    sns.barplot(x=analise.index, y=analise.values)
    plt.title(f'Total de Vendas por {coluna_categoria}')
    plt.xlabel(coluna_categoria)
    plt.ylabel(f'{coluna_valor.replace("_", " ")} (em milhões de U$)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(plt.gcf()) # Exibe o gráfico no Streamlit


# --- FIM DA DEFINIÇÃO DA FUNÇÃO ---

st.write("Abaixo está uma amostra dos dados:")

# st.dataframe() exibe o dataframe de forma interativa.
st.dataframe(df_games.head())

# --- ANÁLISES E GRÁFICOS ---
st.header("Análise de Vendas por Gênero")
plotar_vendas_agrupadas(df_games, 'Genre', 'Global_Sales')

st.header("Análise de Vendas por Plataforma")
plotar_vendas_agrupadas(df_games, 'Platform', 'Global_Sales')

st.header("Análise de Vendas por Editora")
plotar_vendas_agrupadas(df_games, 'Publisher', 'Global_Sales')