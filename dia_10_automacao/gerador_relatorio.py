import pandas as pd

print("--- Iniciando Gerador de Relatórios Automáticos ---")

# 1. Carregar os dados
try:
    df_games = pd.read_csv("dia_07_projeto_vendas_games/datasets/vgsales.csv")
    print("Dataset de vendas carregado com sucesso.")
except FileNotFoundError:
    print("ERRO: Arquivo 'vgsales.csv' não encontrado. Verifique o caminho e a estrutura de pastas.")
    exit() # Para o script se não encontrar o arquivo

# (Aqui faremos as análises)
# --- 2. Análises ---
print("\nRealizando análises...")

# Agrupar por gênero, somar as vendas e transformar o índice em coluna
vendas_por_genero = df_games.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False).reset_index()
print("- Análise por gênero concluída.")

# Agrupar por plataforma, somar as vendas e transformar o índice em coluna
vendas_por_plataforma = df_games.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).reset_index()
print("- Análise por plataforma concluída.")

# (Aqui salvaremos o relatório)
# --- 3. Salvar o Relatório em Excel ---
print("\nSalvando o relatório em arquivo Excel...")

# Definir o nome e o caminho do arquivo de saída
nome_arquivo_excel = "dia_10_automacao/relatorio_vendas_games.xlsx"

# Utilizar o ExcelWriter para salvar os dataframes em abas diferentes
with pd.ExcelWriter(nome_arquivo_excel, engine='openpyxl') as writer:
    vendas_por_genero.to_excel(writer, sheet_name='Vendas_por_Genero', index=False)
    vendas_por_plataforma.to_excel(writer, sheet_name='Vendas_por_Plataforma', index=False)

print(f"Relatório salvo com sucesso em: {nome_arquivo_excel}")

print("\nProcesso finalizado.")