if __name__ != "__main__":
    from ..gestion.crud import guardar  # Import relativo
    from usuarios.gestion.crud import guardar  # import absoluto

    print(__name__)

    def pagar_impuestos():
        print("Pagando impuesto")
        guardar()

if __name__ == "__main__":
    print("Tarea de mantenimiento")
