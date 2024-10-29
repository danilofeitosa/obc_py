num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

#Aritmeticos
sum = num1 + num2 # Soma
sub = num1 - num2 # Subtracao
div = num1 / num2 # Divisao
mul = num1 * num2 # Multiplicacao
mod = num1 % num2 # Resto da Operacao
exp = num1 ** num2 # Exponenciacao

print(mod)
print(f"Resto da divisao de {num1} por {num2}: {mod}")
print(f"Potencia de {num1} por {num2}: {exp}")

# Comparacao
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(f"Os numeros {num1} e {num2} sao iguais?: {equal}")
print(f"O numero {num1} eh maior ou igual a {num2}?: {bigger_equal}")

# Atribuicao
num1 += 1 # num1 = num1 + 1
num1 -= 1 # num1 = num1 - 1
num1 *= 1 # num1 = num1 * 1
num1 /= 1 # num1 = num1 / 1