"""Implementar un algoritmo que reciba un grafo y determine si el mismo es un grafo bipartito, o no. Es decir, la función es_bipartito debe devolver True si el grafo recibido por parámetro es efectivamente bipartito, False en caso contrario. Que un grafo sea Bipartito implica que puede separarse los vértices en dos grupos S y T, tal que para cada par de vértices de S no exista arista entre sí (lo mismo para T), que la intersección entre S y T sea vacía y que la unión sea igual al conjunto de todos los vértices del grafo.

A fines del ejercicio, considerar que se pueden ver todos los vértices del grafo en un orden aleatorio con for v in grafo, y el grafo cuenta con la primitivas hay_arista(origen, destino) (devuelve bool), adyacentes(vertice) que devuelve una lista de vértices adyacentes al indicado, y vertices() que nos devuelve todos los vértices (lista).

El grafo internamente se encuentra implementado con listas de adyacencia (en su versión de diccionario de diccionarios), a considerar para la complejidad."""

def es_bipartito(grafo):
    visitados = set()
    grupo = {}
    for v in grafo:
        if v not in visitados:
            visitados.add(v)
            grupo[v] = 0
            if not es_bipartito_rec(grafo, v, visitados, grupo):
                return False
    return True

def es_bipartito_rec(grafo, v, visitados, grupo):
    for w in grafo.adyacentes(v):
        if w in visitados:
            if grupo[v] == grupo[w]:
                return False
        else:
            visitados.add(w)
            grupo[w] = 1 - grupo[v]
            if not es_bipartito_rec(grafo, w, visitados, grupo):
                return False
    return True