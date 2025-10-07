import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados (nosso ponto de partida)
df_games = pd.read_csv("dia_07_projeto_vendas_games/datasets/vgsales.csv")

print("--- Script de Análise com Funções Reutilizáveis ---")
print("Dataset carregado com sucesso.")

# (Aqui é onde vamos construir nossa função mágica)
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
    plt.show()


# --- FIM DA DEFINIÇÃO DA FUNÇÃO ---

# --- UTILIZANDO A NOSSA FUNÇÃO ---

# Chamada para a Pergunta 1: Quais Gêneros vendem mais?
#plotar_vendas_agrupadas(df_games, 'Genre', 'Global_Sales')

# Chamada para a Pergunta 2: Quais Plataformas vendem mais?
#plotar_vendas_agrupadas(df_games, 'Platform', 'Global_Sales')

# Chamada para a Pergunta 3: Quais Editoras vendem mais?
#plotar_vendas_agrupadas(df_games, 'Publisher', 'Global_Sales')

# Chamada para a Pergunta 4: Quais Anos vendem mais?
plotar_vendas_agrupadas(df_games, 'Year', 'Global_Sales')