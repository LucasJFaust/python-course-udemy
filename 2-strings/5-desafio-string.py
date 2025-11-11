"""
Escreva um programa que leia três notas de um aluno digitados pelo usuário e retorne a média dele.
"""
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

print(f"A média do aluno é: {media:.2f}")