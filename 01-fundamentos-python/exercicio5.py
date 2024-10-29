"""
Exercício 5:
* Conta letras maiúsculas e minúsculas:
-> Escreva uma função Python que receba uma string e Conte o numero de letras maiúsculas e minúsculas desta string.

* Lista números pares e impares de uma lista:
-> Escreva uma função Python para imprimir os números pares e impares em duas listas separadas para cada uma.
em duas listas separadas para cada una.
"""

# 1 - Contar letras maiúsculas e minúsculas
# palavra = input("Digite a palavra a ser analisada: ")
# maiuscula = 0
# minuscula = 0

# for letra in palavra:
#     if (letra.isupper()):
#         maiuscula += 1
#     elif(letra.islower()):
#         minuscula += 1
        
# print(f"Maiúsculas: {maiuscula}")
# print(f"Minúsculas: {minuscula}")
        
def check_char(text):
    type = {"Uppercase": 0, "Lowercase": 0}
    for char in text:
        if char.isupper():
            type["Uppercase"] += 1
        elif char.islower():
            type["Lowercase"] += 1
    print("Texto original: ", text)
    print("Número de letras maiúsculas:", type["Uppercase"])
    print("Número de letras minúsculas:", type["Lowercase"])
    
check_char("A Melhor Forma De Prever o Futuro é Criá-lo")
    
# 2 - Lista números pares e impares de uma lista:
# listaNum = []
# pares = []
# impares = []
# num = 0
# while (num != -1):
#     num = int(input("Digite um número: "))
#     if (num != -1):
#         listaNum.append(num)

# for numero in listaNum:
#     if (numero % 2 == 0):
#         pares.append(numero)
#     else:
#         impares.append(numero)
        
# print(pares)
# print(impares)

# Verifica número par ou ímpar
def check_numbers(numbers):
    pairs = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            pairs.append(number)
        else:
            odd.append(number)
    return pairs, odd
print(check_numbers([1, 2, 4, 6, 5, 7, 11, 20, 13]))