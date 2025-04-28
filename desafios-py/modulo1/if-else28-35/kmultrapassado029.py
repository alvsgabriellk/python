print('José estava na estrada mais um dia')
km = int(input('Quantos km/h José estava na estrada que só era permitido até 80km/h?'))
kmm = km - 80
multa = (km - 80) * 7
if km > 80:
    print('Velocidade máxima ultrapassada, {}km/h alcançado, mínimo era 80km/h.'.format(km))
    print('Sua velocidade foi {}km/h acima do limite, multa aplicada de R${:.2f}.'.format(kmm, multa))
else:
    print('Você está no limite, parabéns!')
print('Fim')