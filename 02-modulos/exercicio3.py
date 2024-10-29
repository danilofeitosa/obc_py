"""
* Verificar conteudo da String
-> Escreva um programa em Python para verificar se uma string contém apenas um determinado conjunto de caracteres (neste caso, a-z,
A-Z e 0-9).
"""
import re

def check_caracter(string):
    rule = re.compile(r"[^a-zA-Z0-9]") # Exemplo de utilizacao: Criar uma rede social que nao eh aceito caracteres especiais
    string = rule.search(string)
    return not bool(string)

print(check_caracter("ADFDSFSFfdsffbf213321"))
print(check_caracter("#@^'{};<>"))