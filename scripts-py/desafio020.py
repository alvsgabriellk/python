import random

passeio1 = input('Qual a ideia 1?')
passeio2 = input('Qual a ideia 2?')
passeio3 = input('Qual a ideia 3?')
passeio4 = input('Qual a ideia 4?')
lista = [passeio1, passeio2, passeio3, passeio4]
random.shuffle(lista) #shuffle embaralha e faz a ordem
print('A ordem vai ser:')
print(lista)