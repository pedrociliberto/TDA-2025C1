# Implementar, por división y conquista, una función que dado un arreglo sin elementos repetidos y casi ordenado (todos los elementos se encuentran ordenados, salvo uno), obtenga el elemento fuera de lugar. Indicar y justificar el orden.

def elemento_desordenado(arr):
	elemDesord, _ = elem_rec(arr, 0, len(arr)-1)
	return elemDesord

def elem_rec(arr, ini, fin):
	# Caso base: si solo queda un elemento, ese es el desordenado
	if ini == fin:
		return arr[ini], False

	mid = (ini + fin) // 2

	if arr[mid] > arr[mid+1]:
		if arr[mid+1] > arr[mid-1]:
			return arr[mid], True
		else:
			return arr[mid+1], True
	elif mid != 0 and arr[mid] < arr[mid-1]:
		if mid >= 1:
			return arr[mid-1], True

	elemIzq, encontradoIzq = elem_rec(arr, ini, mid)
	elemDer, encontradoDer = elem_rec(arr, mid+1, fin)

	if encontradoIzq:
		return elemIzq, True
	elif encontradoDer:
		return elemDer, True
	return -1, False


# T(n) = 2 T(n/2) + O(1) --> log2(2) = 1 > 0 --> O(n)

arr = [4, 3, 6, 10, 13, 19]
print(elemento_desordenado(arr))
