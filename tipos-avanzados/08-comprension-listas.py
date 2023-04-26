usuarios = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# MAP
# Manera elegante de asignar elementos en una nueva lista de un indice específico
# nombres = [usuario[0] for usuario in usuarios]

# Filtrar - Filter
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# Filtrar y transformar
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

# MAP
# nombres = list(map(lambda usuario: usuario[0], usuarios))

# Filter
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
