"""
Escreva um programa que leia um número inteiro digitado pelo usuário e retorne a sua tabuada​
"""
numero = int(input("Digite um número inteiro: "))

print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
print("Tabuada concluída!")