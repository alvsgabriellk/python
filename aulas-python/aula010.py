'''carro = int(input('Gustavo disse que comprou um carro recentemente, vamos ver se ele é novo?, quantos anos o carro de Gustavo tem?'))
if carro <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('Fim')'''
####################################
'''nome = input('Digite aqui seu nome:')
if nome == 'Alice':
    print('Que nome Lindo você tem!')
else:
    print('Que nome normal você tem!')
print('Bom dia, {}'.format(nome))'''
###################################
n1 = float(input('Digite aqui a sua primeira nota:'))
n2 = float(input('Digite aqui a sua segunda nota:'))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}.'.format(m))
if m >=6.0:
    print('A SUA NOTA FOI {:.1f}, E ESTÁ DENTRO DA MÉDIA, PARABÉNS!.'.format(m))
else:
    print('A sua nota foi {:.1f} e está baixa, melhore mais!'.format(m))
print('FIM')
