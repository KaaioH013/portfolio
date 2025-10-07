# --- DEFININDO A FUNÇÃO ---
# Usamos 'def' para definir uma função.
# 'nome' é um PARÂMETRO: um valor que a função espera receber para trabalhar.
def criar_saudacao(nome):
    mensagem = "Olá, " + nome + "! Bem-vindo(a) ao curso."
    return mensagem # 'return' é a resposta que a função nos devolve.

# --- USANDO (ou CHAMANDO) A FUNÇÃO ---

# Chamamos a função e passamos o valor "Caio" para o parâmetro 'nome'.
# O resultado que a função retorna é guardado na variável 'saudacao_para_caio'.
saudacao_para_caio = criar_saudacao("Caio")
print(saudacao_para_caio)

# A grande vantagem: REUTILIZAÇÃO!
saudacao_para_maria = criar_saudacao("Maria")
print(saudacao_para_maria)