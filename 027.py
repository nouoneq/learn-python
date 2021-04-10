# leia o nome completo e mostre apenas o primeiro e ultimo nome

nome = str(input('Qual o seu nome? ')).strip().title()
pri = nome.split()
seg = nome.rsplit()
print('Primeiro nome: {}'.format(pri[0]))
print('Ultimo nome: {}'.format(pri[-1]))
print('Ultimo nome: {}'.format(seg[-1]))