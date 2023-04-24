n1 = input("Ingresa primer numero: ")  # Entrada de un valor por el usuario
n2 = input("Ingresa segundo numero: ")

n1 = int(n1)  # Convertir una cadena a un entero
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Para los números {n1} y {n2},
el resultado de la suma es {suma},
el resultado de la resta es {resta},
el resultado de la multiplicacion es {multi},
el resultado de la division es {div},
"""

print(mensaje)
