largura = float(input('Qual a largura da parede em metros: '))
altura = float(input('Qual a altura da parede em metros: '))

area = largura * altura
tinta = area / 2

print('Sua parede tem a dimensão de {:.1f}X{:.1f} e sua área é de {:.1f}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {:.1f}l de tinta'.format(tinta))