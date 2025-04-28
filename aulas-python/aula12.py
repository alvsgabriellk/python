nome = str(input('Digite aqui seu nome:'))
if nome == 'Alice':
    print('Que nome lindo!')

elif nome == 'Guilherme' or 'Ex':
    print('Que nome feio!')

else:
    print('Que nome normal.')

print('Tenha um bom dia, {}!.'.format(nome))