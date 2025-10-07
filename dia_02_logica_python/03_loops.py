# ----------- LOOP FOR -----------
# Usamos o 'for' quando sabemos quantas vezes queremos repetir algo.
# A função range(5) gera números de 0 a 4.

print("Iniciando contagem com o loop FOR:")
for numero in range(5):
    print("O número da vez é:", numero)


# ----------- LOOP WHILE -----------
# Usamos o 'while' (enquanto) quando queremos repetir algo
# ENQUANTO uma condição for verdadeira.

print("\nIniciando contagem com o loop WHILE:")
contador = 0
while contador < 5:
    print("O valor do contador é:", contador)
    # IMPORTANTE: precisamos atualizar o contador para a condição uma hora se tornar falsa.
    # Se esquecermos a linha abaixo, criamos um LOOP INFINITO!
    contador = contador + 1