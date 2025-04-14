import math
co = float(input('Digite aqui o comprimento do cateto oposto:'))
ca = float(input('Digite aqui o comprimento do cateto adjacente:'))
#hi = (co ** 2 + ca ** 2) ** 1/2  #outra forma de hipotenusa
hi = math.hypot(co, ca)  #item hipotenusa
print('O valor do da hipotenusa vai medir {:.2f}.'.format(hi))