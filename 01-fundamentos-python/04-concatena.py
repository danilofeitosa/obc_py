name = input("Digite o nome do Jogo\n")
yearLaunch = int(input("Digite o ano de lancamento do jogo\n"))
gamePrice = float(input("Digite o preco do jogo\n"))
planIncluded = input("Esta incluso no servico mensal?")

print("###Dados do Jogo###")
print("===================")
# Alternativa 1
print("Nome do Jogo: ", name)
print("Ano de Lancamento: ", yearLaunch)
print("Preco do Jogo: ", gamePrice)
print("Esta incluso no plano?: ", planIncluded)
print()

# Alternativa 2
print("Nome do Jogo: ", name, "\nAno de Lancamento: ", yearLaunch, 
      "\nPreco do Jogo: ", gamePrice, "\nEsta incluso no plano?: ", planIncluded)
print()

# Alternativa 3
print(f"Nome do Jogo: {name} \nAno de Lancamento: {yearLaunch} \nPreco do Jogo: {gamePrice} \nEsta incluso no plano: {planIncluded} ")
print()