"""
Variável é um espaço na memória que armazena um valor, dado ou informação.
Atribuição de variáveis é o processo de associar um nome a um valor.
"""

a = 1
b = 2
c = a + b

print(c)

texto = "Olá, mundo!"
print(texto)

# O type() é uma função que retorna o tipo de dado de uma variável.
print(type(a))  # <class 'int'>
print(type(texto))  # <class 'str'>

a == 2  # Comparação, retorna False

"""
Nomws de variáveis devem ser significativos e descritivos:
- Evite nomes genéricos como 'x' ou 'y'.
- Use nomes que indiquem o propósito da variável, como 'idade', 'nome_usuario', etc.
- Nomes devem começar com uma letra ou underscore (_), e podem conter letras, números e underscores.
- Evite palavras reservadas do Python como 'if', 'for', 'while', etc.
- Use letras minúsculas e se necessário, separe palavras com underscores (snake_case).
- Mantenha consistência no estilo de nomenclatura ao longo do código.
"""