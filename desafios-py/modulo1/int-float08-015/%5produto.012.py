'''preço = float(input('Qual o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
#alterado = preço - novo
novo2 = preço - (preço * 10 / 100)
novo3 = preço - (preço * 20 / 100)
print('O valor do produto que custava R${:.2f}, agora com o desconto de 5% vai custar R$ {:.2f}'.format(preço, novo))
print('O valor de outro produto que era R${:.2f}, agora com o desconto de 10% vai custar R${:.2f}'.format(preço, novo2))
print('Agora, outro produto que custava R${:.2f}, com o desconto de 20% vai passar a custar R${:.2f}'.format(preço, novo3))'''


##########################

print('A Steam está mandando descontos de vários jogos, aqui vai uma lista de jogos que estarão em promoção:')
j1 = float(input('Qual o preço do jogo 1?:'))
j2 = float(input('Qual o preço do jogo 2?:'))
j3 = float(input('Qual o preço do jogo 3?:'))
j1p = 16
j2p = 35
j3p = 9
j1d = j1 - (j1 * j1p / 100)
j2d = j2 - (j2 * j2p / 100)
j3d = j3 - (j3 * j3p / 100)
print('O jogo Stardew Valley que tava por R${} agora com o desconto de {}% vai ficar no valor: R${:.2f}.'.format(j1, j1p, j1d))
print('O jogo Zelda Ocarina of Time que tava por R${} agora com o desconto de {}% vai ficar por: R${:.2f}.'.format(j2, j2p, j2d))
print('O jogo Hollow Knights que tava por R${} agora com o desconto de {}% vai ficar por: R${:.2f}.'.format(j3, j3p, j3d))
