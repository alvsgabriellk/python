soma = 0
cont = 0
print('{:=^40}'.format(' Informações '))
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma de todos {} valores é: {}.'.format(cont, soma))

