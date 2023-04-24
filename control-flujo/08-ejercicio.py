mensaje = """
    Bienvenidos a la calculadora
    Para salir escribe Salir
    Las operaciones son suma, multi, div y resta
"""

print(mensaje)

comando = ""
numero = input("Ingresa número: ")

while True:
    operacion = input("Ingresa operacion:")

    if operacion.lower() == "salir":
        break

    sigNumero = input("Ingresa siguiente numero:")

    if operacion.lower() == "suma":
        numero = float(numero) + float(sigNumero)
    elif operacion.lower() == "multi":
        numero = float(numero) * float(sigNumero)
    elif operacion.lower() == "div":
        numero = float(numero) / float(sigNumero)
    else:
        numero = float(numero) - float(sigNumero)

    print("El resultado es:", numero)
