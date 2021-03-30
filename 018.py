# leia um ângulo e mostre o sin , cos , tan

import math

ang = float(input('Digite um ângulo para mostrar o sin,cos,tan  : '))
sin = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('SIN --> {:.2f}'.format(sin))
print('COS --> {:.2f}'.format(cos))
print('TAN --> {:.2f}'.format(tan))
