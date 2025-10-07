import numpy as np 

array_3d = np.random.randint(101,size=(4,3,2))
print(f'la forma del array es: {array_3d.shape}')
print(f"dimensiones del array: {array_3d.ndim}")
print(f"tamaño del array: {array_3d.size}")
print(f"el tipo de dato es: {array_3d.dtype}")
print(f"el tamaño de cada elemento: {array_3d.itemsize} ")
print(f"tamaño total del array: {array_3d.nbytes}")

print(f"el tamaño total en bytes (nbytes) es igual al producto del número de elementos (size) por el tamaño de cada elemento (itemsize) {array_3d.size * array_3d.itemsize}")