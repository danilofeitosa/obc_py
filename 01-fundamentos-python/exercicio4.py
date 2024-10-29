"""
Exercício 4:
• Contagem Regressiva:
-> Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e disparar um "beep".

• Tabuada:
-> Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário.
"""
import winsound

# Lançamento do Foguete
contagemRegressiva = 10
for i in range(10):
    print(contagemRegressiva)
    contagemRegressiva -= 1
winsound.Beep(2500, 500)
    
# Tabuada
numero = int(input("Tabuada de: "))
numInicial = int(input("De: "))
numFinal = int(input("Até: "))
multiplicador = 1

x = numInicial

while x <= numFinal:
    print(f"Tabuada de {numero} x {x} = {numero * x}")
    x += 1