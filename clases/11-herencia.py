class Animal:
    def comer(self):
        print("Comiendo")


class Perro(Animal):
    '''Herencia'''

    def pasear(self):
        print("Pasenado")


class Chanchito(Perro):
    '''Herencia multinivel'''

    def programar(self):
        print("Programando")
