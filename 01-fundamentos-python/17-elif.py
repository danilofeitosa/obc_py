num1 = float(input("Digite o número 1: "))
num2 = float(input("Digite o número 2: "))
operation = input("Digite a operação a realizar (+ - * /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Operação inválida")
    result = 0
print(f"Resultado é: {result:.2f}") #Para a resposta vir apenas com 2 casas decimais