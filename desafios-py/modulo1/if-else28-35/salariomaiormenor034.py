print('Boa tarde, Sr. Matheus!')
salario = float(input('Quanto é o seu salário mensal?R$'))
if salario > 1250.00:
    aumento10 = salario + (salario*10/100)
    print('O seu salário que era \033[31mR${:.2f}\033[m, agora com o aumento de \033[33m10%\033[m será de \033[32mR${:.2f}\033[m.'.format(salario, aumento10))
else:
    aumento15 = salario + (salario*15/100)
    print('O seu salário que era \033[31mR${:.2f}\033[m, agora com o aumento de \033[33m15%\033[m será de \033[32mR${:.2f}\033[m.'.format(salario, aumento15))