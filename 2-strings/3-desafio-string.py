"""
Escreva um programa que leia o nome completo do usuário e retorne ele em maísculas, minúsculas, capitalizado e 
em formatação de título​
"""
nome_completo = input("Digite seu nome completo: ")

print(f"Nome em maiúsculas: {nome_completo.upper()}")
print(f"Nome em minúsculas: {nome_completo.lower()}")
print(f"Nome capitalizado: {nome_completo.capitalize()}")
print(f"Nome em formato de título: {nome_completo.title()}")
print(f"Número de caracteres (sem espaços): {len(nome_completo.replace(' ', ''))}")
print(f"Número de palavras: {len(nome_completo.split())}") # O split divide a string em palavras
print(f"Primeiro nome: {nome_completo.split()[0]}")
print(f"Último nome: {nome_completo.split()[-1]}")