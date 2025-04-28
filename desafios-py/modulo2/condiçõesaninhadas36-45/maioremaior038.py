n1 = int(input('Escreva aqui o primeiro número:'))
n2 = int(input('Escreva aqui o segundo número:'))
maior = n1
if n1 < n2:
    maior = n2
    print('O segundo é o maior.')
    print('O maior número é o {}.'.format(maior))
if n2 < n1:
    maior = n1
    print('O primeiro é o maior.')
    print('O maior número é o {}.'.format(maior))
elif n1 == n2:
    print('Os dois números são iguais.')
