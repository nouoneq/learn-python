# 10 termos de uma PA

PT = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
calc = PT + (10 - 1)*razao
for c in range(PT,calc+razao,razao):
    print(c, end=" -> ")
print('ACABOU')
