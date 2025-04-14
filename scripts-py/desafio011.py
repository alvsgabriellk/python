larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
área = larg * alt
tinta = área / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.1f}m².'.format(larg, alt, área))
print('Para pintar a sua área de {}m², você vai precisar de {:.1f}L de tinta.'.format(área, tinta))