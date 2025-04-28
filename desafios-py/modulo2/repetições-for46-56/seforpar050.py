print('-'*30)
print('Informações:')
soma = 0
cont = 0
for num in range(1, 7):
    num = int(input('Digite aqui um valor:'))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você informou {} número par e a soma foi {}.'.format(cont, soma))
