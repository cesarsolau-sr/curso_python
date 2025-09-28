print("Por favor ingrese un numero entero")
try:
    numero = int(input())
except ValueError:
    print("Error: Debes introducir un número entero.")
except KeyboardInterrupt:
    print("Se ha interrumpido la ejecución del programa")
else:
    print(f"Has introducido el número: {numero}")