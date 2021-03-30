# leia a largura e a altura de uma parede, em metros, calcule sua área e a quantidade de tinta para pinta-la toda (1L = 2m²).

lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = alt*lar
tinta = area/2
print('A parede tem {:.2}m de altura e {:.2}m de largura a área total a ser pintada é de {:.2}m²'.format(alt,lar,area))
print('para pintar a parede completa será nescessário {:.2}L de tinta'.format(tinta))