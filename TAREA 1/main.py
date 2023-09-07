from clases.registro import Registro
from clases.usuario import Usuario

array=Registro(10)
array.importar()

# Primera visualizacion
print("Inicio")
array.print()
print("----------------------------------------------------------------------------------------")

# Agregar
print("Agregar")
array.agregar(Usuario(11,"A","15/08/09","cali","cr 54 74 15","6036816","@"))
array.agregar(Usuario(15,"B","15/08/09","cali","cr 54 74 15","6036816","@"))
array.agregar(Usuario(13,"C","15/08/09","cali","cr 54 74 15","6036816","@"))
array.agregar(Usuario(18,"D","15/08/09","cali","cr 54 74 15","6036816","@"))
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
