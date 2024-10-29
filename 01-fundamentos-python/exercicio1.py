'''
Exercício 1:
* Antecessor e Sucessor de um número:
-> Escreva um programa em Python que leia um número e represente o número antecessor e sucessor desse número que foi lido, utilizando operadores de atribuição.
* Média de 4 notas:
-> Escreva um programa em Python que leia quatro números e calcule a média entre esses números
'''

# Antecessor e Sucessor

nota1 = int(input("Digite um numero: "))
print(f"O antecessor do numero {nota1} eh {nota1 - 1}")
print(f"O antecessor do numero {nota1} eh {nota1 + 1}")

# Media de 4 notas

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A media das notas {nota1}, {nota2}, {nota3} e {nota4} eh igual a {media}")