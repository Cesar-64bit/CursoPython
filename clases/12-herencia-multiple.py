class Caminador:
    def caminar(self):
        print("Caminando")

    def pasear(self):
        print("Pasenado animales")


class Volador:
    def volar(self):
        print("Volando")


class Nadador:
    def nadar(self):
        print("Nadando")


class Perro(Caminador, Nadador):
    def programar(self):
        print("Programando")


p = Perro()
