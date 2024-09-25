"""
Exercicio 3:
* Cálculo da Distância:
-> Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,35 para viagens mais longas.

* Aumento salário funcionário:
-> Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, de 15%.
"""

distancia = float(input("Digite a distancia a ser percorrida (em km): "))

if distancia <= 200:
    result = distancia * 0.50
else:
    result = distancia * 0.35
    
print(f"A distância de {distancia:.2f} km a ser percorrida vai custar R$ {result:.2f}.")


salario = float(input("Digite o salário: "))

if salario > 1250.00:
    result = salario * 10/100
else:
    result = salario * 15/100
    
print(f"O valor do aumento para o salário de R$ {salario:.2f} é igual a R$ {result:.2f}.")