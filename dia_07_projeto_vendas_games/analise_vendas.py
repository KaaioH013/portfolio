import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o novo dataset
df_games = pd.read_csv("dia_07_projeto_vendas_games/datasets/vgsales.csv")

# Exploração inicial para entender os dados
print("--- 5 Primeiras Linhas do Dataset ---")
print(df_games.head())

print("\n--- Informações Gerais do Dataset ---")
df_games.info()

print("\n--- Verificando valores nulos em cada coluna ---")
# Este comando conta quantos valores nulos (vazios) existem em cada coluna.
print(df_games.isnull().sum())

# --- PERGUNTA 1: QUAIS GÊNEROS VENDEM MAIS? ---

# 1. Agrupar os dados por gênero e somar as vendas globais de cada um.
# .sort_values(ascending=False) ordena do maior para o menor.
vendas_por_genero = df_games.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)

print("\n--- Total de Vendas Globais por Gênero (em milhões) ---")
print(vendas_por_genero)

# 2. Criar o gráfico de barras para visualizar o resultado.
plt.figure(figsize=(12, 6)) # Cria uma figura maior para o gráfico caber bem.
sns.barplot(x=vendas_por_genero.index, y=vendas_por_genero.values)

plt.title('Total de Vendas Globais por Gênero de Jogo')
plt.xlabel('Gênero')
plt.ylabel('Vendas Globais (em milhões de U$)')
plt.xticks(rotation=45) # Rotaciona os rótulos do eixo X para não ficarem uns sobre os outros.
# plt.show()

# --- PERGUNTA 2: QUAIS PLATAFORMAS VENDEM MAIS? ---

# 1. Agrupar os dados por plataforma e somar as vendas globais
vendas_por_plataforma = df_games.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False)

print("\n--- Total de Vendas Globais por Plataforma (em milhões) ---")
print(vendas_por_plataforma)

# 2. Criar o gráfico de barras para a nova análise
plt.figure(figsize=(12, 6)) # Cria uma nova tela para o gráfico
sns.barplot(x=vendas_por_plataforma.index, y=vendas_por_plataforma.values)

plt.title('Total de Vendas Globais por Plataforma')
plt.xlabel('Plataforma (Console)')
plt.ylabel('Vendas Globais (em milhões de U$)')
# plt.show()

# --- PERGUNTA 3: QUAIS EDITORAS VENDEM MAIS? ---

# 1. Agrupar os dados por editora e somar as vendas globais
vendas_por_editora = df_games.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False)

print("\n--- Total de Vendas Globais por Editora (em milhões) ---")
print(vendas_por_editora)

# 2. Criar o gráfico de barras final
plt.figure(figsize=(12, 6)) # Nova tela
sns.barplot(x=vendas_por_editora.index, y=vendas_por_editora.values)

plt.title('Total de Vendas Globais por Editora')
plt.xlabel('Editora')
plt.ylabel('Vendas Globais (em milhões de U$)')
plt.xticks(rotation=45, ha='right') # O 'ha' melhora o alinhamento dos textos rotacionados
plt.tight_layout() # Ajusta o gráfico para garantir que os rótulos não sejam cortados
plt.show()