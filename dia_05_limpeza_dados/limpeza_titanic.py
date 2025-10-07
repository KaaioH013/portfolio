import pandas as pd

# Carregar o dataset a partir do caminho que já conhecemos
caminho_arquivo = "dia_04_pandas/datasets/titanic.csv"
df = pd.read_csv(caminho_arquivo)

print("--- Informações Iniciais (ANTES da Limpeza) ---")
df.info()

# --- TRATANDO A COLUNA 'AGE' ---
# Primeiro, calculamos a média de todas as idades existentes na coluna 'Age'
media_idade = df['Age'].mean()
print(f"\nA idade média calculada (que será usada para preencher) é: {media_idade:.2f} anos")

# Agora, usamos o método .fillna() para preencher os valores vazios (NaN) com a média
# O argumento 'inplace=True' faz a modificação diretamente no nosso DataFrame 'df'.
df['Age'] = df['Age'].fillna(media_idade)

print("Valores de idade que estavam faltando foram preenchidos com a média.")

# --- TRATANDO A COLUNA 'CABIN' ---
# Como a coluna 'Cabin' tem muitos valores ausentes, vamos removê-la (drop).
# O argumento 'axis=1' especifica que estamos removendo uma COLUNA.
# (axis=0 seria para remover uma LINHA).
df.drop('Cabin', axis=1, inplace=True)

print("\nColuna 'Cabin' foi removida.")

# --- VERIFICAÇÃO FINAL ---
print("\n--- Informações Finais (DEPOIS da Limpeza) ---")
df.info()