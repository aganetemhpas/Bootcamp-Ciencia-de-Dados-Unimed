#CONJUNTOS NAO SUPORTAM INDEXAÇÃO - TEM QUE CONVERTER O SET PARA LISTA

numeros = {1, 2, 3, 2}
print(type(numeros))

numeros = list(numeros)

print(numeros[0])
