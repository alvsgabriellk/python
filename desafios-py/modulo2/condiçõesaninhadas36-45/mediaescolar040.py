from time import sleep

print('-=-'*20)
print('Média escolar geral')
print('-=-'*20)
n1 = float(input('Diga a sua primeira nota:'))
n2 = float(input('Diga a sua segunda nota:'))
média = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f} sua média é {:.1f}.'.format(n1, n2, média))

'''if média < 5.0:
    print('Situação...')
    sleep(1.5)
    print('Reprovado.')'''

'''if 7 > média >= 5:
    print('Situação...')
    sleep(1.5)
    print('Reprovado.')'''

if média >= 5 and média < 7:
    print('Situação...')
    sleep(1.5)
    print('Recuperação.')

elif média >= 7.0:
    print('Situação...')
    sleep(1.5)
    print('Aprovado!')

elif média < 5:
    print('Situação...')
    sleep(1.5)
    print('Reprovado.')