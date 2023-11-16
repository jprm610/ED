from clases.binarySearchTree import BinarySearchTree


# Crear un objeto BinarySearchTree
abb = BinarySearchTree()

# Insertar datos en el ABB
abb.insert("Juan", 7)
abb.insert("Pablo", 4)
abb.insert("Maria", 9)
abb.insert("Ana", 2)
abb.insert("Diana", 10)
abb.insert("Mateo", 8)

# Imprimir el árbol antes de eliminar un nodo
print("Árbol Inorder antes de eliminar un nodo:")
print(str(abb))

# Eliminar un nodo del ABB
abb.remove(9)

# Imprimir el árbol después de eliminar un nodo
print("Árbol Inorder después de eliminar un nodo:")
print(str(abb))

# Imprimir metodo find
print(str(abb.find(2)))
# Imprimir metodo max
print(str(abb.maxNode()))

# Imprimir metodo min
print(str(abb.minNode()))
abb.visualize_tree()

