#import math
from math import sqrt
num = int(input('Digite um número:'))
#raiz = math.sqrt(num)
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}.'.format(num, raiz))
#print('A raiz de {} é igual a {:.2f}.'.format(num, math.ceil(raiz)))
# math.ceil arrendondando pra cima e floor pra baixo.