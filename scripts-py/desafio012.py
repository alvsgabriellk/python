preço = float(input('Qual o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
#alterado = preço - novo
novo2 = preço - (preço * 10 / 100)
novo3 = preço - (preço * 20 / 100)
print('O valor do produto que custava R${:.2f}, agora com o desconto de 5% vai custar R$ {:.2f}'.format(preço, novo))
print('O valor de outro produto que era R${:.2f}, agora com o desconto de 10% vai custar R${:.2f}'.format(preço, novo2))
print('Agora, outro produto que custava R${:.2f}, com o desconto de 20% vai passar a custar R${:.2f}'.format(preço, novo3))