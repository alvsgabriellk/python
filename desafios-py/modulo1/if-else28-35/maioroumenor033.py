a = int(input('Primeiro valor:'))
b = int(input('Segundo Valor:'))
c = int(input('Terceiro valor:'))
#testando valor menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor é o {}.'.format(menor))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor é o {}.'.format(maior))