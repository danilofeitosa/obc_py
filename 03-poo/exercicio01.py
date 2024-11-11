"""
* Avaliação e Média de Nota dos Filmes
Desenvolva novas funcionalidades para complementar o nosso gerenciamento da classe Filmes. Segue o escopo das funcionalidades: 
1-Uma das Funcionalidades requeridas é que o usuário possa realizar a avaliação de um filme passando uma nota com parametro e que essa nota seja salva no atributo especifico da classe.

2-Assim que uma avaliação for realizada, deve ser incrementado o total de avaliadores daquele filme. Obs: Considere criar um atributo específico para esse fim.

3-Para cada filme ter uma nota de avaliação média que consiste na divisão do total de avaliação pelo total de avaliadores.
"""

class Movie:
    def __init__(self, name, yearLaunch, includePlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includePlan = includePlan
        self.totalEvaluation = 0
        self.durationMinutes = durationMinutes
        self.evaluators = 0
    
    def __str__(self):
        return f"Filme: {self.name}"
    
    def techinal_sheet(self):
        print("##Dados do Filme##")
        print(f"Nome do Filme: {self.name}")
        print(f"Ano de Lançaento: {self.yearLaunch}")
        print(f"Está no plano? {self.includePlan}")
        print(f"Avaliação do Filme: {self.totalEvaluation}")
        print(f"Duração do Filme: {self.durationMinutes}")
        print(f"Total de Avaliadores: {self.evaluators}\n")
        
    def evaluate(self, note):
        self.totalEvaluation += note 
        self.evaluators += 1
        
    def average(self):
        print(f"Média do Filme: {self.name}: {self.totalEvaluation / self.evaluators}")
        
mario = Movie("Super Mario Bros", 2023, False, 135)
avatar = Movie("Avatar", 2023, False, 220)

mario.evaluate(9.5)
mario.evaluate(10.0)
mario.techinal_sheet()
mario.average()

avatar.evaluate(8.5)
avatar.evaluate(9.0)
avatar.techinal_sheet()
avatar.average()
