buscar = 10

for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado: ", buscar)
        break
else:
    print("No se ha encontrado")

for char in "Ultimate python":
    print(char)
