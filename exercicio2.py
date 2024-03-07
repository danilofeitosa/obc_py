'''
Ex2.1_Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere

Ex:

fifa 23 → **fi#a 23**

restart→ resta#t
'''

nome = "Acarajé"
char = nome[0].lower()
novo_nome = nome.replace(char, "$")
novo_nome = char + novo_nome[1:]
print(novo_nome)

'''
Ex2.2_Escreva um programa Python para obter uma única string de duas strings fornecidas, separadas por um espaço e troque os dois primeiros caracteres de cada string.

Ex:

abc xyz → **xyc abz**
'''

st1 = "abc"
st2 = "xyz"

novo_st1 = st2[:2] + st1[2:]
novo_st2 = st1[:2] + st2[2:]
print(novo_st1)
print(novo_st2)
