"""
Exercicio 2:
* substituindo caractere repetido:
-> Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere.
Ex: fifa 23 -> fi$a 23

* Troca de caracteres:
-> Escreva um programa Python para obter uma única string de duas strings fornecidas separadas por um espaço e troque os dois primeiros caracteres de cada string.
Ex: abc xyz -> xyc abz
"""

name = "Cachorro"
primeiraLetra = name[:1]
primeiraLetraMinuscula = name[:1].lower()
troca = name.replace(primeiraLetraMinuscula,"$")
print(troca)

"""
name = input("Digite o nome do jogo\n)
char = name[0].lower()
newName = name.replace(char, "$")
newName = char + newName[1:]
print(newName)
"""

str1 = "abc" #xyc
str2 = "xyz" #abz
new_st1 = str2[:2] + str1[2:]
new_st2 = str1[:2] + str2[2:]
print(new_st1)
print(new_st2)

