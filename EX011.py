larg = float(input('Largura da Parede: '))
alt = float (input('Altura da Parede: '))
area = larg * alt
print ('Sua parede tem dimensão de {}*{}, e sua area é de {}m2.'.format(larg,alt,area))
tinta = area / 2
print ('Para Pintar Essa Area Voce Precisara de {} Litros de Tinta.'.format(tinta))