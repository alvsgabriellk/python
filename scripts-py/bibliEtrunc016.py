'''from math import trunc
#import math
num = float(input('Digite aqui um número com mais de 2 dígitos:'))
#print('O número que vc digitou é {} e o número inteiro dele é: {}.'.format(num, math.floor(num)))
print('O número digitado é {}, e o número inteiro desse valor é {}.'.format(num, trunc(num)))'''

# outra forma de validar número inteiro
num = float(input('Digite um número aqui:'))
print('O valor digitado é {}, e o valor inteiro é {}.'.format(num, int(num)))