import numpy as np

print(np)
matriz = np.random.rand (3,3)
suma = np.sum(matriz)
resta = np.subtract(matriz,2)
multiplicacion = np.multiply (matriz,3)
transpuesta = np.transpose(matriz)

print ("matriz original")
print (matriz)
print ("suma de la matriz",suma)
print ("resta de la matriz por 2:")
print (resta)
print ("multiplicacion de la matriz por 2:")
print (multiplicacion)
print ("transpuesta de la matriz:")
print (transpuesta)
