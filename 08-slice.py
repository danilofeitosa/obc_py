gameName = "Fifa 23"
gameDescription = """
    Fifa 23 é um jogo de futebol
    desenvolvido pela EA Sports
    e que possibilita jogar local-
    mente ou online.
"""

# string[inicio:fim] - Índice começa na posição 0 / Índice final -1 

# 1 - Busque toda string a partir da primeira posição
print(gameName[0:])

# 2 - Busque toda string até a última posição
print(gameName[:6])

# 3 - Busque toda a string da terceira até a última posição
print(gameName[2:])

"""
string[início:fim:passo] - Índice começa na posição 0 / Índice final -1.
passo - Determina o incremento. Por padrão esse número é o 1.
"""

# 4 - Busque toda a string de 2 em 2 caracteres
print(gameName[::2])

# 5 - Busque toda a string de 3 em 3 caracteres
print(gameName[1::2])

# 6 - Inverta uma string de trás para frente
print(gameName[::-1])