class Perro:
    def habla(self):  # En una clase ya no se llaman funciones, se les llaman métodos
        print("Guau!")


mi_perro = Perro()
mi_perro.habla()
print(isinstance(mi_perro, Perro))
