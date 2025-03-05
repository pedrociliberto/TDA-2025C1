# Se tiene un arreglo tal que [1, 1, 1, …, 0, 0, …] (es decir, unos seguidos de ceros). Se pide una función de orden O(log(n)) que encuentre el índice del primer 0. Si no hay ningún 0 (solo hay unos), debe devolver -1.


def indice_primer_cero(arr):
    return indice_rec(arr, 0, len(arr)-1)

def indice_rec(arr, ini, fin):
    if ini >= fin:
        if arr[ini] == 0:
            return ini
        return -1
    mit = (ini + fin) // 2
    if arr[mit] == 1:
        return indice_rec(arr, mit+1, fin)
    else:
        return indice_rec(arr, ini, mit)
    


arr = [1, 1, 0, 0, 0, 0]
print(indice_primer_cero(arr))