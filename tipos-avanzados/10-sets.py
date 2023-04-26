primer = {1, 1, 2, 2, 3, 4}
# primer.add(5)
# primer.remove(1)
# print(primer)

segundo = [3, 4, 5]
segundo = set(segundo)  # Crea un set en base a una lista

print(primer | segundo)  # Union de los sets
print(primer & segundo)  # Intersección de los sets
print(primer - segundo)  # Diferencia de los sets
print(primer ^ segundo)  # Diferencia simétrica

if 5 in segundo:
    print("Hola mundo")
