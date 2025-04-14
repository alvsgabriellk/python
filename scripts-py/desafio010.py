real = float(input('Digite aqui quanto tem na sua carteira R$'))
dolar = real / 5.98
euro = real / 6.59
print('Com R${:.2f} você consegue comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você consegue comprar EUR${:.2f}'.format(real, euro))
