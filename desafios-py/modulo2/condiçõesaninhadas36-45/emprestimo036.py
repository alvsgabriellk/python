print('-'*20)
print('Empréstimo bancário')
print('-'*20)
casa = float(input('Qual o valor da casa que você tem interesse? R$'))
salario = float(input('Nós diga o seu salário mensal: R$'))
anos = int(input('Quantos anos parcelando a casa?:'))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar a casa no valor de R${:.2f} em {} anos.'.format(casa, anos))
print('O valor da prestação será de R${:.2f}.'.format(prestação))
if prestação <= minimo:
    print('Empréstimo concedido!')
else:
    print('Empréstimo negado.')

