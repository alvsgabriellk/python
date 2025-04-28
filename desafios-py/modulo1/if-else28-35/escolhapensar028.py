from random import randint
from time import sleep
#import random
print('jogo de adivinhação, vamos lá!')
num = int(input('Digite um número entre 0 e 5:  '))
lista = [0, 1, 2, 3, 4, 5]
escolha = random.choice(lista)
if num == escolha:
    print('Parabéns, você acertou, escolheu o número correto!')
else:
    print('Tente de novo, escolhi o número {}, e vc o {}, vc perdeu!'.format(escolha, num))
print('Fim de jogo!')

###############

computador = randint(0, 5) # faz o computador pensar em número inteiro.
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar!...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei?')) # jogador tenta adivinhar
print('Processando...')
sleep(2)
if jogador == computador:
    print('Parabéns!, você acertou o mesmo número que o comnputador!.')
else:
    print('Você errou!, você escolheu o número {}, e o computador o número {}.'.format(jogador, computador))



