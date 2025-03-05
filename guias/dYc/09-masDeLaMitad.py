# Implementar una función (que utilice división y conquista) de orden O(n logn) que dado un arreglo de n números enteros devuelva true o false según si existe algún elemento que aparezca más de la mitad de las veces. Justificar el orden de la solución.

def mas_de_la_mitad(arr):
    if len(arr) == 0:
        return False
    hayMayoritario = mayoritario(arr, 0, len(arr)-1)
    if hayMayoritario is None:
        return False
    # Verificar si el candidato realmente es mayoritario
    countCand = count(arr, 0, len(arr)-1, hayMayoritario)
    return countCand > len(arr) // 2

def mayoritario(v, ini, fin):
    if ini == fin:
        return v[ini]
    
    mit = (ini + fin) // 2
    leftCand = mayoritario(v, ini, mit)
    rightCand = mayoritario(v, mit + 1, fin)
    
    if leftCand == rightCand:
        return leftCand
    
    leftCount = count(v, ini, fin, leftCand)
    rightCount = count(v, ini, fin, rightCand)
    
    # Retorna el candidato con mayor cantidad de ocurrencias
    if leftCount > rightCount:
        return leftCand
    else:
        return rightCand

def count(v, ini, fin, cand):
    cont = 0
    for i in range(ini, fin + 1):
        if v[i] == cand:
            cont += 1
    return cont

# T(n) = 2 T(n/2) + O(n)
# log2(2) = 1 = C = 1 --> Complejidad: O(n log(n))

a1 = [1, 2, 1, 2, 3] # false
a2 = [1, 1, 2, 3] # false
a3 = [1, 2, 3, 1, 1, 1] # true
a4 = [1] # true

print(mas_de_la_mitad(a1))
print(mas_de_la_mitad(a2))
print(mas_de_la_mitad(a3))
print(mas_de_la_mitad(a4))