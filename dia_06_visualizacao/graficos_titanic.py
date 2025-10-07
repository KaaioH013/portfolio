import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar os dados
caminho_arquivo = "dia_04_pandas/datasets/titanic.csv"
df = pd.read_csv(caminho_arquivo)

# 2. Reaplicar a limpeza essencial que fizemos no Dia 5
# Preencher valores nulos de 'Age' com a média
media_idade = df['Age'].mean()
df['Age'] = df['Age'].fillna(media_idade)

# Remover a coluna 'Cabin'
df.drop('Cabin', axis=1, inplace=True)

# 3. Limpeza Adicional: Remover linhas com 'Embarked' nulo
# A coluna 'Embarked' tinha apenas 2 valores faltando. A forma mais
# simples de limpar quando são poucas linhas é simplesmente removê-las.
df.dropna(subset=['Embarked'], inplace=True)

print("--- Dataset limpo e pronto para visualização ---")
df.info()

# --- GRÁFICO 1: Contagem de Sobreviventes ---
print("\nGerando o primeiro gráfico...")

# Define um tema estético para o gráfico (opcional, mas deixa mais bonito)
sns.set_theme(style="darkgrid")

# A função countplot() do Seaborn conta a frequência de cada categoria em uma coluna.
sns.countplot(x='Survived', data=df)

# Usamos o Matplotlib (plt) para adicionar títulos e rótulos, tornando o gráfico mais claro.
plt.title('Contagem de Sobreviventes no Titanic')
plt.xlabel('Sobreviveu (0 = Não, 1 = Sim)')
plt.ylabel('Número de Passageiros')

# Este é o comando que efetivamente abre a janela e exibe o gráfico.
# plt.show()

# --- GRÁFICO 2: Sobreviventes por Sexo ---
plt.figure() # <--- ADICIONE ESTA LINHA PARA CRIAR UMA NOVA TELA
print("\nGerando o segundo gráfico...")
sns.countplot(x='Survived', hue='Sex', data=df)
plt.title('Contagem de Sobreviventes por Sexo')
plt.xlabel('Sobreviveu (0 = Não, 1 = Sim)')
plt.ylabel('Número de Passageiros')
plt.legend(title='Sexo')
# plt.show() # MANTENHA ESTE COMENTADO POR ENQUANTO


# --- GRÁFICO 3: Contagem de Passageiros por Sexo ---
plt.figure() # <--- ADICIONE ESTA LINHA TAMBÉM
print("\nGerando o terceiro gráfico...")
sns.countplot(x='Sex', data=df)
plt.title('Número Total de Passageiros por Sexo')
plt.xlabel('Sexo')
plt.ylabel('Número de Passageiros')
# plt.show() # DEIXE APENAS O ÚLTIMO SHOW ATIVO

# --- GRÁFICO 4: Distribuição de Idades ---
plt.figure() # Criamos uma nova tela limpa
print("\nGerando o último gráfico: Histograma de Idades...")

# sns.histplot() é ideal para ver a distribuição de uma variável numérica.
sns.histplot(data=df, x='Age', bins=30, kde=True)

plt.title('Distribuição de Idades dos Passageiros no Titanic')
plt.xlabel('Idade')
plt.ylabel('Contagem de Passageiros')

plt.show()