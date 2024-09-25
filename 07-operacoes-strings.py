gameDescription = """
    Fifa 23 é um jogo de futebol
    desenvolvido pela EA Sports
    e que possibilita jogar local-
    mente ou online.
"""

gameName = "Fifa"
gameVersion = " 23"
line = "="

# 1 - Operação de Concatenação de Strings
print(line * 25)
gameFullName = gameName + gameVersion
print(gameFullName)

# 2 - Multiplicação de Strings
print(line * 25)

# 3 - Procura palavra dentro de um texto

print("Fifa" in gameDescription)
print("futebol" in gameDescription)