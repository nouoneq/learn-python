# leia duas notas de um aluno
# media < 5.0 = reprovado
# media entre 5.0 e 6.9 = recuperacao
# media > 7.0 = aprovado


n1 = float(input('Diga sua nota1: '))
n2 = float(input('Diga sua nota2: '))
m = (n1+n2)/2
if m < 5.0:
    print('ALUNO REPROVADO!')
elif m >= 5.0 and m <= 6.9:
    print('ALUNO DE RECUPERACAO!')
else:
    print('ALUNO APROVADO!!!')
