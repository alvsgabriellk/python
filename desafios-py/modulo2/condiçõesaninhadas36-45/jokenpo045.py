import random
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada?'))
print('JO')
sleep(0.9)
print('KEN')
sleep(0.9)
print('PO!!!')
print('-='*11)
print('O computador jogou {}.'.format(itens[computador]))
print('O jogador jogou {}.'.format(itens[jogador]))
if computador == 0: # PEDRA
    if jogador == 0:
        print('Jogo deu empate')
    elif jogador == 1:
        print('jogador venceu!')
    elif jogador == 2:
        print('Computador venceu!')
    else:
        print('Tente novamente')

if computador == 1: # PAPEL
    if jogador == 0:
        print('Computador venceu!')
    elif jogador == 1:
        print('Jogo deu empate')
    elif jogador == 2:
        print('Jogador venceu!')
    else:
        print('Tente novamente')
if computador == 2: # TESOURA
    if jogador == 0:
        print('Jogador venceu!')
    elif jogador == 1:
        print('Computador venceu!')
    elif jogador == 2:
        print('Jogo deu empate')
    else:
        print('Tente novamente')
print('-='*11)
