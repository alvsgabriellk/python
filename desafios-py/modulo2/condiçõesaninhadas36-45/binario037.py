num = int(input('Digite aqui um número:'))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADÉCIMAL''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('O valor {} foi convertido para BINÁRIO é igual a: {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O valor {} foi convertido para OCTAL é igual a: {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O valor {} foi convertido para HEXADÉCIMAL é igual a: {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente!.')