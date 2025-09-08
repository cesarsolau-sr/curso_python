cuadrado = lambda x: x**2
es_par = lambda y : y%2 == 0 
suma = lambda a,b : a+b
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(cuadrado,numeros))
pares = list(filter(es_par,numeros))
print(cuadrados)
print(pares)