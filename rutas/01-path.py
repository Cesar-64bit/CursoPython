from pathlib import Path

# Path(r"C:\Archivos de Programa\Minecraft")  # Windows
# Path("one/__init__.py")

path = Path("hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

# Cambiar nombres a los arhcivos con todo, incluyendo la extención
p = path.with_name("chanchito.exe")
print(p)
p = path.with_suffix(".bat")
print(p)
p = path.with_stem("felix")
print(p)
