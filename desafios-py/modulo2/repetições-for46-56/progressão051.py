primeiro = int(input('Escreva aqui o primeiro termo:'))
razão = int(input('Razão:'))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão): # a razão do  meio é ate onde vai
    print('{}'.format(c), end=' -> ')
print('ACABOU')