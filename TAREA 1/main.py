from clases.registro import Registro
from clases.usuario import Usuario

array = Registro(2)
#array.agregar(Usuario(1,"Andres","16/07/00","Medellin"))
array.agregar( Usuario(1,"Meli"))
array.agregar(Usuario(2,"Pablito"))
array.eliminar(1)
for i in array.usuarios:
    print(i.id,i.nombre)