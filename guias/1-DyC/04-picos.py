# Se tiene un arreglo de N >= 3 elementos en forma de pico, esto es: estrictamente creciente hasta una determinada posición p, y estrictamente decreciente a partir de ella (con 0 < p < N - 1). Por ejemplo, en el arreglo [1, 2, 3, 1, 0, -2] la posición del pico es p = 2. Implementar un algoritmo de división y conquista de orden O(log n) que encuentre la posición p del pico.

def posicion_pico(v, ini, fin):
    if ini >= fin:
        return ini
    mit = (ini+fin)//2
    if v[mit] > v[mit-1] and v[mit] > v[mit+1]:
        return mit
    elif v[mit] < v[mit+1]:
        return posicion_pico(v, mit+1, fin)
    else:
        return posicion_pico(v, ini, mit)
    
# T(n) = T(n/2) + O(1) --> Complejidad: O(log(n))
    
def pico(v):
    return posicion_pico(v, 0, len(v)-1)

v = [1, 2, 3, 14, 0, -2]
print(pico(v))