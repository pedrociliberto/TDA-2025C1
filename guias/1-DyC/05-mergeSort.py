# Implementar el algoritmo de Merge Sort.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mit = len(arr)//2

    izq = merge_sort(arr[:mit])
    der = merge_sort(arr[mit:])

    return merge(izq, der)

def merge(a1, a2):
    i, j = 0, 0
    merged = []

    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            merged.append(a1[i])
            i += 1
        else:
            merged.append(a2[j])
            j += 1

    while i < len(a1):
        merged.append(a1[i])
        i += 1
    while j < len(a2):
        merged.append(a2[j])
        j += 1

    return merged

# T(n) = 2 T(n/2) + O(n) --> Complejidad: O(n log(n))

v = [14, 5, 45, 2, 8, 9, 98, 25, 13, 8]
print(merge_sort(v))