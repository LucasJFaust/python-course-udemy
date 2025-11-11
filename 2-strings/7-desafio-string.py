"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.​
"""
largura = float(input('Largura da parede (em metros): '))
altura = float(input('Altura da parede (em metros): '))

area = largura * altura
tinta_necessaria = area / 2

print(f'A área da parede é {area:.2f} m² e a quantidade de tinta necessária é {tinta_necessaria:.2f} litros.')