def parte_entera_raiz(n):
    if n == 0 or n == 1:
        return n
    return raiz_aux(n, 0, n)

def raiz_aux(n, ini, fin):
    if ini > fin:
        return fin
    mit = (ini+fin)//2

    if mit*mit == n:
        return mit
    elif mit*mit < n:
        return raiz_aux(n, mit+1, fin)
    else:
        return raiz_aux(n, ini, mit-1)
    
# T(n) = T(n/2) + O(1) --> Complejidad: O(log(n))


print(parte_entera_raiz(9))
print(parte_entera_raiz(16))
print(parte_entera_raiz(28))
print(parte_entera_raiz(10))
print(parte_entera_raiz(90))