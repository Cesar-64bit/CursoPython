numeros = [2, 3, 4, 1, 9, 8, 7]

# numeros.sort()  # Ordenar de manera ascendente
# numeros.sort(reverse=True)  # Ordenar de manera descendente

# # Ordena ascendentemente creando una nueva copia del arreglo (no afecta al original)
# numeros2 = sorted(numeros)
# # Ordena descendente creando una nueva copia del arreglo (no afecta al original)
# numeros2 = sorted(numeros, reverse=True)

print(numeros)

# Ordena listas que contienen listas
# usuarios = [[4, "Chanchito"], [1, "Felipe"], [5, "Pulga"]]
# usuarios.sort()

usuarios = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]

usuarios.sort(key=lambda el: el[1])


print(usuarios)
