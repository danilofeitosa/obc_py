gameName = "Fifa23"
gameDescription = """
Fifa 23 é um jogo de futebol, desenvolvido pela EA Sports,
e que possibilita jogar local mente ou online.
"""

print(gameName.upper()) # Retornar string em maiúsculo.
print(gameName.lower()) # Retornar string em minúsculo.
print(gameName.capitalize()) # Apenas a primeira letra em maiúsculo.
print(gameName.title()) # Apenas a primeira letra em maiúsculo.
print(gameName.center(10, '-')) # Retornar a string centralizada com caractere de preenchimento.
print(gameName.find("i")) # Retorna a posição de um determinado caractere.
print(gameName.count("f")) # Conta caracteres.
print(gameDescription.count("f")) # Conta caracteres.
print(gameDescription.count("a")) # Conta caracteres.
print(gameDescription.replace("Fifa", "Pes")) # Altera um elemento por outro.
print(gameDescription.split(",")) # Quebra a String em um determinado ponto, excluindo-o.



