n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 //n2
e = n1 ** n2
print('A soma é {},\n o produto é {}, e a divisão é {:.3f}.'.format(s, m, d), end=' >>> ')
#{:.3f} signfica que dps da virgula/ponto vai só três casas dps.
#end= serve para não quebrar a linha com o print ou tlvz mais.
# o \n serve para quebrar a linha.
print('Divisão inteira {}, e potência {}.'.format(di, e))