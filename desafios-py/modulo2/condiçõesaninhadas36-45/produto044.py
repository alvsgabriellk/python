print('{:=^40}'.format(' LOJA ALVES '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual a opção?'))
if opção == 1:
    saldo = preço - (preço * 10 / 100)
    print('Com o desconto de 10%, você vai pagar R${:.2f}.'.format(saldo))
elif opção == 2:
    saldo = preço - (preço * 5 / 100)
    print('Com o desconto de 5%, você vai pagar R${:.2f}.'.format(saldo))
elif opção == 3:
    print('Você vai pagar o preço normal, R${:.2f}.'.format(preço))
    parcela = preço / 2
    print('Sua compra vai ser parcelada em 2 vezes de R${:.2f}.'.format(parcela))
elif opção == 4:
    saldo = preço + (preço * 20 /100)
    print('Com o juros de 20%, você vai pagar R${:.2f}.'.format(saldo))
    parcela = saldo / 2
    print('Sua compra vai ser parcelada em 3 vezes de R${:.2f}.'.format(parcela))
else:
    total = 0
    print('Opção inválida de pagamento.')









'''print('Olá!, aqui vai algumas perguntas:')
print('-'*30)
produton = float(input('Qual o valor do produto?R$'))
dinheiro = str(input('Vai pagar com dinheiro?'))
cheque = str(input('Vai pagar em cheque?'))
cartãov = str(input('Vai pagar a vista no cartão?'))
cartãox = str(input('Vai pagar parcelado no cartão?'))
print('-'*30)

if dinheiro or cheque:
    produtot = produton - (produton * 10 / 100)
    print('O produto que era R${:.2f}, agora com o desconto de 10% vai ficar por R${:.2f}'.format(produton, produtot))
elif cartãov:
    produtot = produton - (produton * 5 / 100)
    print('O produto que era R${:.2f}, agora com o desconto de 5% vai ficar por R${:.2f}.'.format(produton, produtot))'''