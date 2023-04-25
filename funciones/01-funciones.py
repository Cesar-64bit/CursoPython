# Función con parámetros opcionales
def hola(nombre, apellido="Gomez"):
    print("Hola mundo!")
    print(f"Bienvenido {nombre} {apellido}")


hola("César", "Bernal")
hola("Nadia")

# Función con argumentos nombrados
hola(apellido="Perez", nombre="Oswaldo")

# Función con parámetros
# def hola(nombre, apellido):
#     print("Hola mundo!")
#     print(f"Bienvenido {nombre} {apellido}")


# hola("César", "Bernal")
# hola("Nadia", "Gomez")
