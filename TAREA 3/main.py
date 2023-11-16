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

# Imprimir el recorrido inorder para verificar la construcción del ABB
abb.inorder(abb.get_root())