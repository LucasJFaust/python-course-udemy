"""
1. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado, a
quantidade de dias pelos quais ele foi alugado e se o cliente faz parte do programa de
fidelidade da loja. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15
por Km rodado para clientes não participantes do programa de fidelidade e R$ 58 a diária mais R$0,05
por Km rodado para clientes participantes do programa de fidelidade.
"""
# km_percorridos = float(input("Digite a quantidade de Km percorridos: "))
# dias_alugados = int(input("Digite a quantidade de dias alugados: "))
# fidelidade = input("O cliente faz parte do programa de fidelidade? (s/n): ").strip().lower()
# valor_diaria_n = 60
# valor_km_n = 0.15
# valor_diaria_s = 58
# valor_km_s = 0.05

# if fidelidade == 's':
#     total = (valor_diaria_s * dias_alugados) + (valor_km_s * km_percorridos)
# else:
#     total = (valor_diaria_n * dias_alugados) + (valor_km_n * km_percorridos)

# print(f"O valor total a pagar é: R$ {total:.2f}")

"""
2. Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import datetime

ano_de_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = datetime.now().year
idade = ano_atual - ano_de_nascimento
tempo_para_alistamento = 18 - idade
if idade < 18:
    print(f"Ainda faltam {tempo_para_alistamento} anos para o alistamento.")
elif idade == 18:
    print("Está na hora exata de se alistar.")
else:
    print(f"Já passou {abs(tempo_para_alistamento)} anos do prazo de alistamento.")

