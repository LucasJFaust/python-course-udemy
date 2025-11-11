"""
Operadores Aritiméticos

Operadores aritméticos são usados para realizar operações matemáticas comuns,
como adição, subtração, multiplicação e divisão.
"""
a = 10
b = 3
soma = a + b          # Adição
subtracao = a - b     # Subtração
multiplicacao = a * b # Multiplicação
divisao = a / b       # Divisão (resultado é float)
divisao_inteira = a // b  # Divisão inteira (resultado é int)
modulo = a % b        # Módulo (resto da divisão)
exponenciacao = a ** b  # Exponenciação
exemplo = 2 * 5 + 3 - 4 / 2 ** 2  # Exemplo de expressão complexa. Podemos notar que a ordem de precedência é respeitada com a multiplicação e divisão sendo realizadas antes da adição e subtração.

print("Soma:", soma)                     # 13
print("Subtração:", subtracao)           # 7
print("Multiplicação:", multiplicacao)   # 30
print("Divisão:", divisao)               # 3.3333...
print("Divisão Inteira:", divisao_inteira) # 3
print("Módulo:", modulo)                 # 1
print("Exponenciação:", exponenciacao)   # 1000
print("Exemplo de expressão complexa:", exemplo)
"olá mundo" + "!"  # Exemplo de concatenação de strings
print("Concatenação de strings:", "olá mundo" + "!")  # olá mundo!
print("curso de Python" * 3)  # Exemplo de repetição de strings

# Calculo do IMC
peso = 70  # Peso em kg
altura = 1.75  # Altura em metros
imc = peso / (altura ** 2)  # Cálculo do IMC
print("IMC:", imc)  # Exibe o IMC calculado
print("IMC formatado:", round(imc, 2))  # Exibe o IMC formatado com duas casas decimais