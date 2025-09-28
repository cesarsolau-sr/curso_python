import os 
import sys

def formato_tamaño_legible(tamaño_bytes):
    """Convierte un tamaño en bytes a un formato legible (KB, MB, GB)."""
    for unidad in ['B', 'KB', 'MB', 'GB', 'TB']:
        if tamaño_bytes < 1024 or unidad == 'TB':
            return f"{tamaño_bytes:.2f} {unidad}"
        tamaño_bytes /= 1024


lista_elementos = os.listdir()
print(os.getcwd())
print(lista_elementos)
lista_archivos = []
for item in os.listdir():
    if os.path.isfile(item):
        archivo = {}
        archivo["nombre"]= item
        archivo["peso"] = os.path.getsize(item)
        lista_archivos.append(archivo)
lista_ordena = sorted(lista_archivos,key=lambda d: d['peso'], reverse=True)
for arch in lista_ordena:
    print(f"archivo:{arch['nombre']} peso:{formato_tamaño_legible(arch['peso'])} ")

print(sys.path)


