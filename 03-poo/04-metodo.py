class Movie:
    def __init__(self, name, yearLaunch, includePlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includePlan = includePlan
        self.note = note
        self.durationMinutes = durationMinutes
    
    def __str__(self):
        return f"Filme: {self.name}"
    
    def techinal_sheet(self):
        print("##Dados do Filme##")
        print(f"Nome do Filme: {self.name}")
        print(f"Ano de Lançaento: {self.yearLaunch}")
        print(f"Está no plano? {self.includePlan}")
        print(f"Avaliação do Filme: {self.note}")
        print(f"Duração do Filme: {self.durationMinutes}\n")
        
mario = Movie("Super Mario Bros", 2023, False, 5.0, 125)
top_gun = Movie("Top Gun", 2022, True, 4.5, 160)

mario.techinal_sheet()
top_gun.techinal_sheet()