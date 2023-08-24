from clases.registro import Registro
from clases.usuario import Usuario

array = Registro(5)
array.agregar(Usuario(1,"A"))
array.agregar(Usuario(5,"B"))
array.agregar(Usuario(3,"C"))
array.agregar(Usuario(3,"D"))
#array.agregar(Usuario(2,"D"))
#array.agregar(Usuario(6,"D"))

#print(array.buscarUsuario(1))
#print(array.buscarPosicion(1))

""" for u in array.usuarios :
    if u != None :
        print(u.id, u.nombre) """