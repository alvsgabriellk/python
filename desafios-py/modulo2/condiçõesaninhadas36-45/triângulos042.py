print('-=-'*20)
print('Analisador de triângulos')
print('-=-'*20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
print('Segue informações sobre o triângulo:')
print('-'*20)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O segmento acima podem formar triângulo.')
    if r1 == r2 == r3: # ou r1 == r2 and r2 == r3
        print('- Equilátero: Todos os lados são iguais.')
    elif r1 == r2 or r2 == r3 or r3 == r1: # OU r1 != r2 != r3 != r1   PQ È DIFERENTE COM O !
        print('- Isósceles: Dois lados iguais.')
    else:
        print('- Escaleno: Todos os lados são diferentes.')
else:
    print('O segmento acima não podem formar triângulo.')
print('-'*20)