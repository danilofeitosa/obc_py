# 1 - Função para imprimir Hello World
def welcome():
    print("Hello World")
    
welcome()

# 2 - Função para somar dois números
def sum():
    return 5+4

print(sum())

# - Função para cadastrar um jogo
def create_game():
    name = input("Digite o nome do Jogo: ")
    yearLaunch = int(input("Digite o ano de lancamento do jogo: "))
    gamePrice = float(input("Digite o preco do jogo: "))
    planIncluded = input("Esta incluso no servico mensal?: ")
    
    print(f"{name} - R$ {gamePrice}")
    
create_game()
create_game()