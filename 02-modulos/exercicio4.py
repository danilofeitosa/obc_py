
"""
* Advinhe o Número
-> Escreva um programa em Python que gera um número aleatório para que o usuário tente acertar o número. Algumas sugestões para o programa:
1 - Utilizar um laço de repetiçào para que o programa execute até que o usuário informe um número referente a opcão para sair do programa.
2 - Utilizar o módulo random para gerar valores aleatórios dentro de um intervalo. Ex: 1 a 10.
3 - Lé o número que o usuário digitar via input e comparar se é o mesmo número que o programa sorteou.
"""
import random

done = False

while not done:
    print("O que deseja fazer agora?")
    print("1. Adivinhar o número")
    print("2. Sair")
    
    choice = input("> ")
    
    if choice == "1":
        print("=====Adivinhe um número de 1 a 10=====")
        number = int(input("Digite um número de 1 a 10: "))
        result = random.randint(1, 10)
        if number == result:
            print("Parabéns. Você acertou!")
        else:
            print(f"Tente novamente. O número sorteado foi {result}")
    elif choice == "2":
        done = True
    else:
        print("Opção inválida. Escolha uma opção entre 1 e 2!")