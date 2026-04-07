# Neyder Fabián Peña González Codigo:2252004
# Julio Cesar Sierra Jimenez  Codigo:2251503

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

class Arbol:
    def __init__(self, raiz):
        self.raiz = Nodo(raiz)

    def buscar(self, nodo, valor):
        if nodo.valor == valor:
            return nodo
        for hijo in nodo.hijos:
            encontrado = self.buscar(hijo, valor)
            if encontrado:
                return encontrado
        return None

    def insertar(self, padre, valor):
        nodo_padre = self.buscar(self.raiz, padre)
        if nodo_padre:
            nodo_padre.hijos.append(Nodo(valor))
            print("Se agregó")
        else:
            print("no se encontró")

    def peso(self, nodo):
        total = 1
        for hijo in nodo.hijos:
            total += self.peso(hijo)
        return total

    def orden(self, nodo):
        max_hijos = len(nodo.hijos)
        for hijo in nodo.hijos:
            max_hijos = max(max_hijos, self.orden(hijo))
        return max_hijos

    def altura(self, nodo):
        if len(nodo.hijos) == 0:
            return 1
        return 1 + max(self.altura(hijo) for hijo in nodo.hijos)


# PROGRAMA PRINCIPAL

raiz = input("Ingrese la raíz del árbol: ")
arbol = Arbol(raiz)

while True:
    print("\n   MENÚ   ")
    print("1. Insertar nodo")
    print("2. Peso del árbol")
    print("3. Orden del árbol")
    print("4. Altura del árbol")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            padre = input("Ingrese el valor del nodo padre: ")
            valor = input("Ingrese el nuevo nodo: ")
            arbol.insertar(padre, valor)

        case "2":
            print("Peso:", arbol.peso(arbol.raiz))

        case "3":
            print("Orden:", arbol.orden(arbol.raiz))

        case "4":
            print("Altura:", arbol.altura(arbol.raiz))

        case "5":
            print("Saliendo...")
            break

        case _:
            print("Opción inválida")
