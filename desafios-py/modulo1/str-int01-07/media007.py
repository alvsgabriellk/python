'''b1 = float(input('O aluno Cauã Gabriell no primeiro bimestre tirou a nota:'))
b2 = float(input('No segundo bimestre ele tirou a nota:'))
média = (b1 + b2) / 2
#total = media / 2
print('A média entre {} e {} ficou no total: {}.'.format(b1, b2, média))'''

###################
aluno = input('Digite aqui o nome do aluno:')
b1 = float(input('O aluno {} no primeiro bimestre tirou a nota:'.format(aluno)))
b2 = float(input('E no segundo bimestre {} tirou a nota:'.format(aluno)))
tb1 = (b1 + b2) / 2
b3 = float(input('No terceiro bimestre {} tirou a nota:'.format(aluno)))
b4 = float(input('E no quarto bimestre {} tirou a nota:'.format(aluno)))
tb2 = (b3 + b4) / 2
print('A média do primeiro semestre de {} ficou de {:.1f}.'.format(aluno, tb1))
print('A média no segundo semestre de {} ficou de {:.1f}.'.format(aluno, tb2))