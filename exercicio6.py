"""
Exercicio Final:
* Gerenciamento de Jogadores e Times.
-> Escreva um programa em python que realize o gerenciamento de jogadores.
Ele deve atender aos seguintes requisitos:

1 - A opção de listar os times deve mostrar o índice, o nome e a quantidade de jogadores do time.
2 - A opção de adicionar un time deve pedir um nome para o time que será cadastrado.
3 - A opção de remover um time deve pedir o índice específico do time que foi cadastrado para fazer a sua exclusão.

4 - A opção de adicionar um jogador em um time deve pedir um índice do time que foi cadastrado e associar com o nome do jogador que será adicionado.
5 - A opção de remover un jogador em um time deve pedir um índice do time que foi cadastrado e utilizar esse índice para remover o jogador que fora cadastrado no time.
6 - A opção de listar os jogadores de um time deve ser informado o índice de um time e listar os jogadores que foram associados a ele.

Obs: Este é o exercício de final do módulo, então aproveite para utilizar todos os recursos vistos até agora, as funções, condições, loop, listas, etc.
"""


listaTimes = []
indice = 1
opcao = input("Digite a opcao desejada: ")
while (opcao != "0"):
    if opcao == "1":
        print("--- Lista de Times ---")
        print(listaTimes)
        opcao = input("Digite a opcao desejada: ")
    elif opcao == "2":
        print("--- Adicionar um time ---")
        nome = input("Digite o nome do Time: ")
        adicionarJogador = True
        time = {
            "nome": nome,
            "indice": indice, 
            "Jogadores": []
        }
        qtdJogadores = int(input("Quantidade de Jogadores a ser incluídos: "))
        contador = 0
        while(contador < qtdJogadores):
            nomeJogador = input("Digite o nome do(s) Jogadores: ")
            time["Jogadores"].append(nomeJogador)
            contador += 1
        listaTimes.append(time)
        print(time)
        indice += 1
        opcao = input("Digite a opcao desejada: ")
    elif opcao == "3":
        print("--- Remover um Time ---")
        remover = int(input("Digite o número do índice do time a ser removido: "))
        for time in listaTimes:
            if time["indice"] == remover:
                listaTimes.remove(time)
                print(f"Time {time} removido com sucesso!")
            else:
                print(f"Não foi encontrado time com o indice {indice}")
        opcao = input("Digite a opcao desejada: ")
    elif opcao == "4":
        print("--- Adicionar Jogador ---")
        adicionar = int(input("Digite o número do índice do time do qual o jogador será adicionado: "))
        for time in listaTimes:
            if time["indice"] == adicionar:
                adicionarJogador = input("Qual o nome do Jogador a ser adicionado: ")
                time["Jogadores"].append(adicionarJogador)
                print(f"Jogador {adicionarJogador} adicionado com sucesso ao time {time["nome"]}!")
            else:
                print(f"Não foi encontrado time com o indice {indice}")
        opcao = input("Digite a opcao desejada: ")
    elif opcao == "5":
        print("--- Remover Jogador ---")
        remover = int(input("Digite o número do índice do time do qual o jogador será removido: "))
        for time in listaTimes:
            if time["indice"] == remover:
                removerJogador = input("Qual o nome do Jogador a ser removido: ")
                time["Jogadores"].remove(removerJogador)
                print(f"Jogador {removerJogador} do {time["nome"]} removido com sucesso!")
            else:
                print(f"Não foi encontrado time com o indice {indice}")
        opcao = input("Digite a opcao desejada: ")
    elif opcao == "6":
        print("---Listar Jogadores---")
        listar = int(input("Digite o número do índice do time do qual o(s) jogador(es) será(ão) listados: "))
        if time["indice"] == listar:
            print(f"Lista de Jogadores do {time["nome"]}: {time["Jogadores"]}")
        else:
            print(f"Não foi encontrado time com o indice {indice}")
        opcao = input("Digite a opcao desejada: ")
            
        
    
                
print("Até logo! :D")