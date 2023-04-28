from pathlib import Path

path = Path("rutas")
# path.exists()
# path.mkdir()  # make directory
# path.rmdir()  # remove directory
# path.rename("Chanchito-feliz")

# iterar
# for p in path.iterdir():
#     print(p)

archivos = [p for p in path.iterdir() if not p.is_dir()]
archivos = [p for p in path.glob("01-*.py")]
archivos = [p for p in path.glob("**/*.py")]  # Todos los arhcivos

print(archivos)
