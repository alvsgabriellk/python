from datetime import date
atual = date.today().year
nasc = int(input('Digite aqui o ano que você nasceu:'))
idade = atual - nasc
print('Sua idade é {}.'.format(idade))
print('-'*25)
print('Catégorias:')
print('Mirim até 9 anos')
print('Infantil até 14 anos')
print('júnior até 19 anos')
print('Sênior até 25 anos')
print('Master acima de 25 anos')
print('-'*25)
if idade <= 9:
    print('Sua catégoria é: MIRIM')
elif 9 < idade and idade <= 14:
    print('Sua catégoria é: INFANTIL')
elif 14 < idade and idade <= 19:
    print('Sua catégoria é: JÚNIOR')
elif 19 < idade and idade <= 25:
    print('Sua catégoria é: SÊNIOR')
elif idade > 25:
    print('Sua catégoria é: MASTER')
