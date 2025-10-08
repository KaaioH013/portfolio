# 🤖 Projeto 2: Gerador de Relatórios em Excel

## 📖 Descrição

Este projeto consiste em um script de automação em Python que realiza uma análise de dados do dataset de vendas de videogames e exporta os resultados para um relatório em formato `.xlsx` (Excel).

O script executa duas análises principais:
1.  Soma das vendas globais por gênero de jogo.
2.  Soma das vendas globais por plataforma (console).

Cada uma dessas análises é salva em uma aba separada dentro do mesmo arquivo Excel, tornando o relatório organizado e fácil de consumir.

## 🚀 Tecnologias Utilizadas

- Python
- Pandas
- Openpyxl

## ⚙️ Como Executar

1.  Certifique-se de que as dependências (`pandas`, `openpyxl`) estão instaladas.
2.  No terminal, a partir da pasta raiz do portfólio, execute o comando:
    ```bash
    python dia_10_automacao/gerador_relatorio.py
    ```
3.  Ao final da execução, um novo arquivo chamado `relatorio_vendas_games.xlsx` será criado dentro desta pasta.