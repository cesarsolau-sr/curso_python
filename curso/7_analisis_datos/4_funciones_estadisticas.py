import numpy as np

temperaturas = np.array([
    [25, 28, 30, 32, 29, 27, 26, 25, 24, 28, 31, 30, 29, 28, 27, 29, 30, 31, 32, 33, 34, 31, 29, 28, 27, 26, 25, 24, 25, 26],  # Ciudad A
    [18, 17, 19, 20, 21, 20, 19, 18, 17, 16, 15, 16, 17, 18, 19, 20, 21, 22, 21, 20, 19, 18, 17, 16, 15, 14, 15, 16, 17, 18],  # Ciudad B
    [31, 32, 33, 34, 35, 36, 35, 34, 33, 32, 31, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 38, 36, 34, 32, 30, 31, 32, 33]   # Ciudad C
])

temp_media = np.mean(temperaturas, axis=1)
print(f"La temperatura media de la ciudad A es:{temp_media[0]:.2f}")
print(f"La temperatura media de la ciudad B es:{temp_media[1]:.2f}")
print(f"La temperatura media de la ciudad C es:{temp_media[2]:.2f}")

max_ciudad = np.max(temperaturas,axis=1)
min_ciudad = np.min(temperaturas,axis=1)

print(f"La temperatura máxima de la ciudad A es:{max_ciudad[0]}")
print(f"La temperatura mínima de la ciudad A es:{min_ciudad[0]}")
print(f"La temperatura máxima de la ciudad B es:{max_ciudad[1]}")
print(f"La temperatura mínima de la ciudad B es:{min_ciudad[1]}")
print(f"La temperatura máxima de la ciudad C es:{max_ciudad[2]}")
print(f"La temperatura mínima de la ciudad C es:{min_ciudad[2]}")

mediana_ciudad = np.median(temperaturas, axis=1)

print(f"La mediana de la temperatura de la ciudad A es:{mediana_ciudad[0]}")
print(f"La mediana de la temperatura de la ciudad B es:{mediana_ciudad[1]}")
print(f"La mediana de la temperatura de la ciudad C es:{mediana_ciudad[2]}")

q1 = np.percentile(temperaturas,25,axis=1)
q3 = np.percentile(temperaturas,75,axis=1)
iqr = q3 - q1
print(f"Rango intercuartílico (IQR) de la ciudad A: {iqr[0]}")
print(f"Rango intercuartílico (IQR) de la ciudad B: {iqr[1]}")
print(f"Rango intercuartílico (IQR) de la ciudad C: {iqr[2]}")

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
print(f"Límite inferior para outliers de la ciudad A: {limite_inferior[0]}")
print(f"Límite superior para outliers de la ciudad A: {limite_superior[0]}")
print(f"Límite inferior para outliers de la ciudad B: {limite_inferior[1]}")
print(f"Límite superior para outliers de la ciudad B: {limite_superior[1]}")
print(f"Límite inferior para outliers de la ciudad C: {limite_inferior[2]}")
print(f"Límite superior para outliers de la ciudad C: {limite_superior[2]}")

# Identificar outliers
maska = (temperaturas[0] < limite_inferior[0]) | (temperaturas[0] > limite_superior[0])
outliersA = temperaturas[0,maska]
print(f"Outliers ciudad A: {outliersA}")

#outliersB = temperaturas[(temperaturas[1] < limite_inferior[1]) | (temperaturas > limite_superior[1])]
maskb = (temperaturas[1] < limite_inferior[1]) | (temperaturas[1] > limite_superior[1])
outliersB = temperaturas[1,maskb]
print(f"Outliers ciudad B: {outliersB}")

#outliersC = temperaturas[(temperaturas[2] < limite_inferior[2]) | (temperaturas > limite_superior[2])]
maskc = (temperaturas[2] < limite_inferior[2]) | (temperaturas[2] > limite_superior[2])
outliersC = temperaturas[2,maskc]
print(f"Outliers ciudad C: {outliersC}")

