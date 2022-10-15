#Não retorna duplicados - Elimina itens duplicados

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

letras = sorted(set("abacaxi")) #Em ordem alfabetica

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}
