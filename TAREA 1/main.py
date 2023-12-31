from clases.registro import Registro
from clases.fecha import Fecha
from clases.direccion import Direccion
from clases.usuario import Usuario

array=Registro(10)
array.importar()

# Primera visualizacion
print("Inicio")
array.print()
print("----------------------------------------------------------------------------------------")

# Agregar
print("Agregar")
array.agregar(Usuario(11,"A",Fecha('15','08','09'),"cali",Direccion('cr','54','74-15','Laureles','Medellin'),"6036816","@"))
array.agregar(Usuario(15,"B",Fecha('15','08','09'),"cali",Direccion('cr','54','74-15','Laureles','Medellin'),"6036816","@"))
array.agregar(Usuario(13,"C",Fecha('15','08','09'),"cali",Direccion('cr','54','74-15','Laureles','Medellin'),"6036816","@"))
array.agregar(Usuario(18,"D",Fecha('15','08','09'),"cali",Direccion('cr','54','74-15','Laureles','Medellin'),"6036816","@"))
array.print()
print("----------------------------------------------------------------------------------------")

# Buscar
print("Buscar")
print(f"Por posicion: {array.buscarPosicion(1).toString()}")
print(f"Por id: {array.buscarUsuario(8).toString()}")
print("----------------------------------------------------------------------------------------")

# Eliminar
print("Eliminar")
array.eliminar(3)
array.eliminar(2)
array.print()
print("----------------------------------------------------------------------------------------")

array.tofile()
