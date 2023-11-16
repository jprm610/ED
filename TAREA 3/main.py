from clases.binarySearchTree import BinarySearchTree


# Crear un objeto BinarySearchTree
abb = BinarySearchTree()

# Insertar datos en el ABB
abb.insert("Juan", 10101013)
abb.insert("Pablo", 10001011)
abb.insert("Maria", 10101015)
abb.insert("Diana", 10111105)
abb.insert("Ana", 1010000)
abb.insert("Mateo", 1011005)

# Imprimir el árbol antes de eliminar un nodo
print("Árbol Inorder antes de eliminar un nodo:")
print(str(abb))

# Eliminar un nodo del ABB
#abb.remove(2)

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

