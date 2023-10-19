from mensajeria.contacto import Contacto
from mensajeria.empleado import Empleado

class Administrador(Empleado) :
    def __init__(self, nombre, cedula, contraseña, fechaNacimiento, ciudadNacimiento, contacto: Contacto) -> None:
        super().__init__(nombre, cedula, contraseña, fechaNacimiento, ciudadNacimiento, contacto)

    def agregarUsuario(self) :
        pass

    def cambiarContraseña(self,empleado,newPassword) :
        empleado.self.contraseña=newPassword
        return empleado.self.contraseña

    def eliminarUsuario(self) :
        pass
