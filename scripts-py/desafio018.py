import math
ângulo = float(input('Digite aqui o ângulo:'))
seno = math.sin(math.radians(ângulo)) #sin é seno
cosseno = math.cos(math.radians(ângulo)) #cos é cosseno
tangente = math.tan(math.radians(ângulo)) #tan é tangente
print('O ângulo de {}, tem o seno de {:.2f}.'.format(ângulo, seno))
print('O ângulo de {}, tem cosseno de {:.2f}.'.format(ângulo, cosseno))
print('O ângulo de  {} tem o tangente de {:.2f}.'.format(ângulo, tangente))