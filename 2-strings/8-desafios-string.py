"""
# 01 -Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
"""
# tem_f = float(input("Digite a temperatura em graus Fahrenheit: "))
# tem_c = (tem_f - 32) * 5 / 9
# print(f"A temperatura em graus Celsius é: {tem_c:.2f}°C")
"""
02 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

o produto do dobro do primeiro com metade do segundo .

a soma do triplo do primeiro com o terceiro.

o terceiro elevado ao cubo.
"""
# n_1 = int(input("Digite o primeiro número inteiro: "))
# n_2 = int(input("Digite o segundo número inteiro: "))
# n_3 = float(input("Digite um número real: "))
# produto = (2 * n_1) * (n_2 / 2)
# soma = (3 * n_1) + n_3
# cubo = n_3 ** 3

# print(f"O produto do dobro do primeiro com metade do segundo é: {produto}")
# print(f"A soma do triplo do primeiro com o terceiro é: {soma}")
# print(f"O terceiro elevado ao cubo é: {cubo:.2f}")
"""
03 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58
"""
# altura = float(input("Digite a altura da pessoa em metros: "))
# peso_ideal = (72.7 * altura) - 58
# print(f"O peso ideal para uma altura de {altura:.2f} metros é: {peso_ideal:.2f} kg")

"""
05 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa
que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos
além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as
mensagens adequadas.
"""
# limite = 50
# peso_de_peixes = float(input("Digite o peso de peixes em quilos: "))
# if peso_de_peixes > limite:
#     excesso = peso_de_peixes - limite
#     multa = excesso * 4.00
#     print(f"João pescou {peso_de_peixes:.2f} kg, que excede o limite de {limite} kg")
#     print(f"Logo, ele deve pagar uma multa de R$ {multa:.2f} por {excesso:.2f} kg excedentes.")
# else:
#     print(f"João pescou {peso_de_peixes:.2f} kg, que está dentro do limite de {limite} kg. Não há multa a pagar.")

"""
06 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto
de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.

quanto pagou ao INSS.

quanto pagou ao sindicato.

o salário líquido.

calcule os descontos e o salário líquido, conforme mostrado abaixo:

+ Salário Bruto : R$

- IR (11%) : R$

- INSS (8%) : R$

- Sindicato ( 5%) : R$

= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.

"""

"""
07 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas
e o preço total.
"""

"""
08 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

comprar apenas latas de 18 litros;

comprar apenas galões de 3,6 litros;

misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

"""
09 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
(em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_link_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))

# Convertendo a velocidade de Mbps para MBps (1 byte = 8 bits)
velocidade_link_mbps_to_mbps = velocidade_link_mbps / 8 # em MBps
tempo_download_segundos = tamanho_arquivo_mb / velocidade_link_mbps_to_mbps
tempo_download_minutos = tempo_download_segundos / 60
print(f"O tempo aproximado de download do arquivo é: {tempo_download_minutos:.2f} minutos")
