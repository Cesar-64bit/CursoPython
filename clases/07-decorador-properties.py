class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    @property  # Transforma al método en una propiedad
    def nombre(self):
        print("Pasa por getter")
        return self.__nombre

    @nombre.setter  # se crea con el decorador property
    def nombre(self, nombre):
        print("Pasando por setter")
        if nombre.strip():
            self.__nombre = nombre
        return


perro = Perro("Choclo")
print(perro.nombre)
