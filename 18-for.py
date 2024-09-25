# 1 - Iterando valores de uma lista.
gamesList = ["Fifa", "God of War", "Red Dead 2", "Uncharted", 90.50]
for game in gamesList:
    print(game)
    
# 2 - Quando a condição for atendida, o Loop será encerrado.
for game in gamesList:
    if game == "Red Dead 2":
        break
    print(game)
    
# 3 - QUando a condição for atendida, o Loop vai para a próxima iteração.
for game in gamesList:
    if game == "Red Dead 2":
        continue
    print(game)
    
# 4 - Avaliação do jogo
gameName = input("Digite o nome do Jogo: ")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo: "))

sum = 0
for i in range(gameRating):
    note = float(input("Digite a nota para o jogo: "))
    sum += note
print(f"Média de avaliação do jogo {gameName} é {sum / gameRating:.2f}")