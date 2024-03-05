gameDescription = """
Fifa 2023 é um jogo de futebol
desenvolvido pela EA Sports e
que possibilita jogar localmente 
ou online.
"""
gameName = "Resident Evil"
gameVersion = " 8"


# 1 - Operação de Concatenação de Strings
gameFullName = gameName + gameVersion
print(gameFullName)

# 2 - Operação de Multiplicação de Strings
line = "="
print(line * 25)

# 3 - Procura palavra-chave dentro de um texto.
print("Fifa" in gameDescription)  #Existe ocorrência de Fifa na gameDescription?
print("futebol" in gameDescription)


