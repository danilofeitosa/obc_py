name = input("Digito o nome do jogo:\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo:\n"))
gamePrice = float(input("Digite o preço do jogo:\n"))
planIncluded = input("Está incluso no serviço mensal?:\n")

#Alternativa 1

# print("###Dados do Jogo###")
# print("===================")
# print("Nome do Jogo:", name)
# print("Ano do Jogo:", yearLaunch)
# print("Preço do Jogo:", gamePrice)
# print("Está incluso no plano?:", planIncluded)

#Alternativa 2

# print("###Dados do Jogo###")
# print("===================")
# print("Nome do Jogo:", name, "\nAno do Jogo:", yearLaunch, "\nPreço do Jogo:", gamePrice, "\nEstá incluso no plano?:", planIncluded)

#Alternativa 3

print(f"Nome do Jogo: {name} \nAno de Lançamento: {yearLaunch} \nPreço do Jogo: {gamePrice} \nEstá incluso no plano?: {planIncluded}")