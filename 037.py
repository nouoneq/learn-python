# leia um numero inteiro e escolha entre (binario,octal ou hexadecimal) para conversao.

esc = input('''\033[1;33m
1 - BINARIO
2 - OCTAL
3 - HEXADECIMAL
0 - TODOS\033[m
\033[0;35m~$\033[m ''')
if esc == '1':
    n1 = int(input('\033[0;32mDIGITE UM NUMERO DECIMAL:\033[m '))
    print('DECIMAL: {}\nBINARIO: {}'.format(n1,bin(n1).replace('0b', '')))
elif esc == '2':
    n1 = int(input('\033[0;32mDIGITE UM NUMERO DECIMAL:\033[m '))
    print('DECIMAL: {}\nOCTAL: {}'.format(n1,oct(n1).replace('0o', '')))
elif esc == '3':
    n1 = int(input('\033[0;32mDIGITE UM NUMERO DECIMAL:\033[m '))
    print('DECIMAL: {}\nHEXADECIMAL: {}'.format(n1,hex(n1).upper().replace('0X', '')))
elif esc == '0':
    n1 = int(input('\033[0;32mDIGITE UM NUMERO DECIMAL:\033[m '))
    print('DECIMAL: {}\nBINARIO: {}\nOCTAL: {}\nHEXADECIMAL: {}'.format(n1,bin(n1).replace('0b', ''),oct(n1).replace('0o', ''),hex(n1).upper().replace('0X', '')))
else:
    print('\033[0;31mOPCAO INVALIDA!\033[m')
