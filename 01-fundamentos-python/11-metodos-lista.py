gamesList = ["Resident Evil 4", "Star Wars Jedi Survivor",
            "The Legend of Zelda", "Red Dead 2", "Mario Odyssey"]

# 1 - Tamanho da Lista.
print(len(gamesList))

# 2 - Recuperar um item da lista pelo índice.
print(gamesList.index("Mario Odyssey"))

# 3 - Adicionar item ao final da lista.
print(gamesList.append("GTA V"))
print(gamesList)

# 4 - Ordenar a Lista.
gamesList.sort()
print(gamesList)

# 5 - Copiar os itens de uma lista para outra.
gamesReset = gamesList.copy()
gamesReset.remove("Star Wars Jedi Survivor")
print(gamesReset)

# 6 - Remove todos os itens da lista.
gamesList.clear()
print(gamesList)