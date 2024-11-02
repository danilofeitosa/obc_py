import hashlib

# 1 - Verificar os algoritmos disponíveis
print(hashlib.algorithms_available)

# 2 - Algoritmos disponíveis de acordo com o Sistema Operacional
print(hashlib.algorithms_guaranteed)

# 3 - Ultilizando o Sha256
algoritm = hashlib.sha256()
print(algoritm.digest())
message = "A melhor forma de prever o futuro é criá-lo".encode()
algoritm.update(message)
print(algoritm.hexdigest())

# 4 - Utilizando o MD5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())