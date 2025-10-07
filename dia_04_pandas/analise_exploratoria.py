# Passo 1: Importar a biblioteca, dando a ela o "apelido" de pd. É uma convenção universal.
import pandas as pd

# Passo 2: Especificar o caminho onde nosso arquivo de dados está guardado.
caminho_do_arquivo = "dia_04_pandas/datasets/titanic.csv"

# Passo 3: Usar a função read_csv() do Pandas para ler o arquivo e carregá-lo em um DataFrame.
# A variável 'df' (abreviação de DataFrame) agora contém nossa tabela inteira.
df = pd.read_csv(caminho_do_arquivo)

# Passo 4: Vamos dar uma espiada nos dados para ver se carregou certo.
# O comando .head() mostra as 5 primeiras linhas do DataFrame.
print("--- As 5 primeiras linhas dos dados do Titanic ---")
print(df.head())

# .shape nos diz as dimensões do DataFrame (linhas, colunas)
print("\n--- Dimensões do DataFrame ---")
print(df.shape)

# .info() nos dá um resumo técnico: nome das colunas, tipos de dados e valores não nulos.
# É ótimo para encontrar colunas com dados faltando!
print("\n--- Informações Técnicas do DataFrame ---")
df.info()

# .describe() nos dá um resumo estatístico das colunas NUMÉRICAS.
print("\n--- Resumo Estatístico das Colunas Numéricas ---")
print(df.describe())