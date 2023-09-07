from clases.registro import Registro
from clases.usuario import Usuario

array=Registro(6)
array.agregar(Usuario(9,"C","15/08/09","cali","cr 54 74 15","6036816","@"))
array.agregar(Usuario(8,"C","15/08/09","cali","cr 54 74 15","6036816","@"))
array.agregar(Usuario(7,"C","15/08/09","cali","cr 54 74 15","6036816","@"))
array.tofile()