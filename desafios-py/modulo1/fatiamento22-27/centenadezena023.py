num = int(input('Digite aqui um número de 10000 a 9999999:'))
'''u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando seu número {}.'.format(num))
print('Unidade: {}.'.format(u))
print('Dezena: {}.'.format(d))
print('Centena: {}.'.format(c))
print('Milhar: {}.'.format(m))'''

dm = num // 10000 % 10
cm = num // 100000 % 10
mm = num // 1000000 % 10
dmm = num // 1000000 % 10
print('Analisando seu número {}.'.format(num))
print('Dezena de milhar: {}.'.format(dm))
print('Centena de milhar: {}.'.format(cm))
print('Milhão: {}.'.format(mm))
print('Dezena de milhão: {}.'.format(dmm))