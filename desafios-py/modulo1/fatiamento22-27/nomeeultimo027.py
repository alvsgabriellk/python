n = str(input('Digite aqui seu nome completo:')).strip()
nome = n.split()
print('Analisando seu nome...')
print('Prazer em te conhecer!')
print('Seu primeiro nome é: {}.'.format(nome[0]))
print('Seu último nome é: {}.'.format(nome[len(nome)-2])) # vai analisar o nome, com o - vai ir indicando da direita para esquerda
