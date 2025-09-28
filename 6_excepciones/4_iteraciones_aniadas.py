
print("Iniciando programa")
matriz = []
for i in range(1,6):
    fila=[]
    for j in range(1,6):
        fila.append(i*j)
    matriz.append(fila)

# Imprimimos la tabla de forma ordenada
for fila in matriz:
    # Usamos join para formatear cada fila como una cadena de texto
    print(" ".join(f"{num:4}" for num in fila))