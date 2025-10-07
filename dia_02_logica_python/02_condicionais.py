media_aluno = 4
tem_presenca_suficiente = True

# O 'and' exige que AMBAS as condições sejam verdadeiras
if media_aluno >= 7.0 and tem_presenca_suficiente:
    print("Parabéns! Aluno Aprovado!")

# Senão, se a média for maior ou igual a 5.0
elif media_aluno >= 5.0:
    print("Atenção. Aluno em Recuperação.")

# Em qualquer outro caso
else:
    print("Infelizmente, aluno Reprovado.") 