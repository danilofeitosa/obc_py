"""
* Classe Produto e metodo desconto 
Desenvolva uma classe em Python para atender as seguintes especificidades de um Produto: 

1 - Cada produto deve ter um preço e nome. 
2 - A classe deve ter un método construtor e o método dundle str. 
3- A classe deve ter um método para desconto. O método deve receber o desconto em percentual e realizar o cálculo de quanto ficaria o preço final con o desconto.
"""

class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco
    
    def __str__(self):
        return f"Nome do Produto: {self.nome}"
    
    def desconto(self, desconto):
        valorDisconto = self.preco * (desconto/100)
        precoFinal = self.preco - valorDisconto
        print(f"Preço final do produto {self.nome} = {precoFinal}")
        
lapis = Produto("Lápis", 5.0)
print(lapis)
lapis.desconto(10)
        