""" La Escuela Nacional 32 "Alan Turing" de Bragado tiene una forma particular de requerir que los alumnos formen fila. En vez del clásico "de menor a mayor altura", lo hacen primero con alumnos yendo con altura decreciente, hasta llegado un punto que empieza a ir de forma creciente, hasta terminar con todos los alumnos.

Por ejemplo las alturas podrían ser 1.2, 1.15, 1.14, 1.12, 1.02, 0.98, 1.18, 1.23.

Implementar una función indice_mas_bajo que dado un arreglo/lista de alumnos(*) que represente dicha fila, devuelva el índice del alumno más bajo, en tiempo logarítmico. Se puede asumir que hay al menos 3 alumnos. En el ejemplo, el alumno más bajo es aquel con altura 0.98.

Implementar una función validar_mas_bajo que dado un arreglo/lista de alumnos(*) y un índice, valide (devuelva True o False) si dicho índice corresponde al del alumno más bajo de la fila. (Aclaración: esto debería poder realizarse en tiempo constante) """

def indice_mas_bajo(alumnos):
    return indice_mas_bajo_rec(alumnos, 0, len(alumnos) - 1)

def indice_mas_bajo_rec(alumnos, inicio, fin):
    if inicio == fin:
        return inicio
    mit = (inicio + fin) // 2
    if validar_mas_bajo(alumnos, mit):
        return mit
    if alumnos[mit].altura < alumnos[mit + 1].altura:
        return indice_mas_bajo_rec(alumnos, inicio, mit)
    else:    
        return indice_mas_bajo_rec(alumnos, mit + 1, fin)


def validar_mas_bajo(alumnos, indice):
    menor_ant = alumnos[indice].altura < alumnos[indice - 1].altura
    menor_sig = alumnos[indice].altura < alumnos[indice + 1].altura
    if indice == 0:
        return menor_sig
    if indice == len(alumnos) - 1:
        return menor_ant
    return menor_ant and menor_sig

# Ejemplo
class Alumno:
    def __init__(self, nombre, altura):
        self.nombre = nombre
        self.altura = altura

alumnos = [Alumno('Juan', 1.70), Alumno('Pedro', 1.60), Alumno('Maria', 1.75), Alumno('Ana', 1.85)]
print(indice_mas_bajo(alumnos)) # 1


