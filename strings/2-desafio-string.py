"""
Escreva um programa que leia o ano de nascimento do usuário e retorne quantos anos ele fará em 2035​
"""
nome_usuario = input("Digite seu nome: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual =2025
ano_futuro = 2035

idade_atual = ano_atual - ano_nascimento
idade_futura = ano_futuro - ano_nascimento
print(f"Este ano {ano_atual} o {nome_usuario} fez {idade_atual} anos. Em 2035 ele fará {idade_futura} anos.")