"""
Exercicio Final:
* Gerenciamento de Jogadores e Times.
-> Escreva um programa em python que realize o gerenciamento de jogadores. Ele deve atender aos seguintes requisitos:

1 - A opção de listar os times deve mostrar o índice, o nome e a quantidade de jogadores do time.
2 - A opção de adicionar un time deve pedir um nome para o time que será cadastrado.
3 - A opção de remover um time deve pedir o índice específico do time que foi cadastrado para fazer a sua exclusão.

4 - A opção de adicionar um jogador em um time deve pedir um índice do time que foi cadastrado e associar com o nome do jogador que será adicionado.
5 - A opção de remover un jogador em um time deve pedir um índice do time que foi cadastrado e utilizar esse índice para remover o jogador que fora cadastrado no time.
6 - A opção de listar os jogadores de um time deve ser informado o índice de um time e listar os jogadores que foram associados a ele.

Obs: Este é o exercício de final do módulo, então aproveite para utilizar todos os recursos vistos até agora, as funções, condições, loop, listas, etc.
"""

teams ={}
done = False

#Função para listar times
def print_teams():
    print("Times Listados: ")
    for i, team in enumerate(teams.values()):
        print(f"{i + 1}. {team['name']} ({len(team['players'])} jogadores)")
        
# Função para listar jogadores de um time
def print_team_players(team):
    print(f"Jogadores do {team['name']}: ")
    for i, player in enumerate(team['players']):
        print(f"{i + 1}. {player}")

while not done:
    # Opções no programa.
    print("O que você deseja fazer?")
    print("1. Adicionar um time")
    print("2. Remover um time")
    print("3. Listar times")
    print("4. Adicionar jogador em um time")
    print("5. Remover jogador em um time")
    print("6. Listar jogadores de um time")
    print("7. Sair")
    
    choice = input("> ")
    if choice == "1":
        team_name = input("Digite o nome do time: ")
        teams[team_name] = {'name': team_name, 'players': []}
        print("Time adicionado.")
    elif choice == "2":
        team_num = int(input("Informe o número do time que deseja remover: "))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num - 1]
            del teams[team_name]
            print("Time removido.")
    elif choice == "3":
        print_teams()
    elif choice == "4":
        print_teams()
        team_num = int(input("Informe o número do time que deseja adicionar o jogador: "))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num - 1]
            player_name = input("Informe o nome do jogador: ")
            teams[team_name]['players'].append(player_name)
            print("Jogador adicionado no time")
        else:
            print("Nome do time está inválido.")
    elif choice == "5":
        print_teams()
        team_num = int(input("Informe o número do time que deseja listar os jogador: "))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num - 1]
            print_team_players(teams[team_name])
            player_num = int(input("Informe o número do jogador que deseja remover: "))
            if player_num <= len(teams[team_name]['players']):
                del teams[team_name]['players'][player_num - 1]
                print("Jogador removido do time.")
            else:
                print("Número do jogador inválido.")
    elif choice == "6":
        print_teams()
        team_num = int(input("Informe o número do time que deseja listar os jogador: "))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num - 1]
            print_team_players(teams[team_name])
        else:
            print("Número do time inválido.")
    elif choice == "7":
        done = True
    else:
        print("Opção inválida!")