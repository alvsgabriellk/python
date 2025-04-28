'''print('Alice e sua familia estavam viajando para Pipa.')
distancia = int(input('Qual foi a distancia percorrida?:'))
if distancia <=200:
    pkm = distancia * 0.50
    print('A distancia percorrida foi {}km, e o valor da passagem ficou de R${:.2f}.'.format(distancia, pkm))
else:
    pkm2 = distancia * 0.45
    print('A distancia percorrida foi {}km, e o valor da passagem ficou com desconto de 5 centavos, total de R${:.2f}.'.format(distancia, pkm2))'''
#MEU
####################
#GUSTAVO

print('Você está prestes a começar uma viagem')
distancia = int(input('Qual a distancia percorrida?:'))
if distancia <=200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print('Você vai percorrer uma distancia de {}km, e vai pagar R${:.2f} a passagem.'.format(distancia, passagem))