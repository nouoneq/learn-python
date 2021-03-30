# Digite algo e mostre as caracteristicas da variavel.

var = input('DIGITE ALGO: ')

print('O TIPO PRIMITIVO DE {} EH: {}'.format(var,type(var)))
print('ESTÁ EM CAPS-LOCK? ',var.isupper())
print('IS LOWER? ',var.islower())
print('É PRINTAVEL? ',var.isprintable())
print('É UM NÚMERO? ',var.isnumeric())
print('É ALFANUMERICO? ',var.isalnum())