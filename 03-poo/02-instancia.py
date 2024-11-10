# https://www.themoviedb.org/?language=pt-br

class Movie:
    name = ""
    yearLaunch = 0
    includePlan = False
    note = 0
    durationMinutes = 0
    
# Primeiro Filme
movie = Movie()
movie.name = "Super Mario Bros"
movie.yearLaunch = 2023
movie.includePlan = False
movie.note = 5.0
movie.durationMinutes = 130
print(">>>> Dados do Filme <<<<")
print()
print(f"Nome do filme: {movie.name} \nAno de Lancamento: {movie.yearLaunch}")
