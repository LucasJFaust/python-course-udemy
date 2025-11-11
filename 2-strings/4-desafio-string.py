"""
Escreva um programa que leia um número digitado pelo usuário e retorne o seu antecessor e o seu sucessor.
Vamos considerar como antecessor o número inteiro imediatamente inferior ao número digitado e como sucessor o
inteiro imediatamente superior ao número digitado
"""
numero = float(input("Digite um número: "))
antecessor = numero - 1
sucessor = numero + 1

print(f"Antecessor: {antecessor}")
print(f"Sucessor: {sucessor}")