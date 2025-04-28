nome = str(input('Digite aqui seu nome todo:')).strip()
print('Analisando seu nome...')
print('Seu nome todo em maiúsculas é: {}.'.format(nome.upper()))
print('Seu nome todo em minúsculas é: {}.'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' '))) #identificar os espaços do meio ou em geral e tirar eles.
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {}, e ele tem {} letras.'.format(separa[0], len(separa[0])))