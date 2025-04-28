frase = str(input('Digite aqui alguma frase:')).strip().upper()
print('Analisando a sua frase...')
print('A letra A aparece {} vezes na frase.'.format(frase.count('A'))) # mandar toda frase maiuscula pra o count entender melhor
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1)) # o + 1 serve pra dizer que a posição certa é um valor depois
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1))