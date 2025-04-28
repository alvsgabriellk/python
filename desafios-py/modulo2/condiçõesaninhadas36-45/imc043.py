peso = float(input('Digite aqui quanto você pesa:'))
alt = float(input('Digite aqui a sua altura:'))
imc = peso / (alt * alt) # OU alt ** 2
print('Segue abaixo informações sobre seu IMC:')
print('-'*20)
print('Seu imc é {:.2f}.'.format(imc))
if imc <= 18.5:
    print('Você está abaixo do peso')
elif imc <= 25:
    print('Você está no peso ideal.')
elif imc <= 30:
    print('Você está sobrepeso.')
elif imc <= 40:
    print('Você está com obesidade.')
elif imc >= 40:
    print('Você está com obesidade mórbida.')