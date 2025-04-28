print('-'*42)
print('Informações:')
num1 = int(input('Digite aqui o valor que vai multiplicar:'))
print('-'*42)
print('{:=^40}'.format(' TABUADA '))
for c in range(1, 11):
    print('{} x {} = {}'.format(num1, c, num1*c))
print('='*40)

