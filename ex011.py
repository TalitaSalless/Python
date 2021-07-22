# 11 Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área de tinta necessária para
# pinta-la, sabendo que cada litro de tinta pinta uma área de 2m2.
largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
tinta = area / 2
print(f'A dimensão da parede é {area}m²')
print(f'Voce irá usar {tinta} litros de tinta')