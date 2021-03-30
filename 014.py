# conversor de graus Celcius para graus Fahrenheit.

celcius = float(input('Digite a temperatura em celcius para ser mostrada em Fahrenheit:'))
fahrenheit = (celcius*9/5) + 32
print('{}⁰C  >>>  {}⁰F '.format(celcius,fahrenheit))