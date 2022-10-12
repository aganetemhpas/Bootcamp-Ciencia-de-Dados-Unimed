lista = [1, "Python", [40, 30, 20]]

lista2 = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

#Mostrando que as Listas são diferentes
print(id(lista), id(lista2))

#Verificando que o que acontece em lista2 não modifica lista1
lista2[0] = 'Adicionei'

print(lista)
print(lista2)