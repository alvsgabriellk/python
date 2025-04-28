dia = int(input('Quantos dias alugados?'))
km = int(input('Quantos km rodados?'))
#totaldia = dia * 60
#totalkm = km * 0.15
total = (dia * 60) + (km * 0.15)
print('Olá!, saiba que a diária é 60 reais, e o km rodado é 0,15 centavos!.')
print('O total a pagar é de R${:.2f}.'.format(total))