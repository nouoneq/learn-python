preco = float(input('VALOR DO PRODUTO: R$'))
esc = str(input('''
[0] \033[1;33mA VISTA DINHEIRO\033[m       - \033[0;32m10% DESCONTO\033[m
[1] \033[1;33mA VISTA CARTAO\033[m         - \033[0;32m5%  DESCONTO\033[m
[2] \033[1;33mATE 2x NO CARTAO\033[m       - \033[0;32mPRECO NORMAL\033[m
[3] \033[1;33mACIMA DE 3x NO CARTAO\033[m  - \033[0;32m20% DE JUROS\033[m
\033[0;35m~$\033[m'''))
if esc == '0':
    desc = preco-(preco*0.10)
    print('PRODUTO:     R${:.2f}\nDESCONTO:    10%\nVALOR FINAL: R${:.2f}'.format(preco,desc))
elif esc == '1':
    desc = preco-(preco*0.05)
    print('PRODUTO:     R${:.2f}\nDESCONTO:    5%\nVALOR FINAL: R${:.2f}'.format(preco,desc))
elif esc == '2':
    print('VALOR DO PRODUTO: R${:.2f}'.format(preco))
elif esc == '3':
    parc = int(input('QUANTAS PARCELAS? '))
    acres = preco+(preco*0.20)
    print('PRODUTO:     R${:.2f}\nJUROS:       20%\nPARCELAS:    R${:.2f}\nVALOR FINAL: R${:.2f}'.format(preco,acres/parc,acres))
else:
    print('OPCAO INVALIDA!')
