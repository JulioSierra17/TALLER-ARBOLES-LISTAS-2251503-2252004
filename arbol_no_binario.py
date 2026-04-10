from bigtree import Node, print_tree

abuelo = Node("Abuelo Juan")

# Creamos a los hijos del abuelo (los padres)
mama = Node("Mamá Carmen", parent=abuelo)
tio = Node("Tío Pedro", parent=abuelo)

hijo1 = Node("Hijo Mayor", parent=mama)
hijo2 = Node("Hermana Menor", parent=mama)
primo = Node("Primo Luis", parent=tio)

print_tree(abuelo)