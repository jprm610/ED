from mensajeria.contacto import Contacto
from mensajeria.empleado import Empleado

class Administrador(Empleado) :
    def __init__(self, nombre, cedula, contraseña, fechaNacimiento, ciudadNacimiento, contacto: Contacto) -> None:
        super().__init__(nombre, cedula, contraseña, fechaNacimiento, ciudadNacimiento, contacto)

    def agregarUsuario(self) :
        pass

    def cambiarContraseña(self,empleado,newPassword) :
        empleado.contraseña=newPassword
        return empleado.contraseña

    def eliminarEmpleado(self, cedula, sistema):
        empleado_borrar = None
        tmp = sistema.credenciales.head

        while tmp:
            if tmp.getData().cedula == cedula:
                empleado_borrar = tmp.getData()
                sistema.credenciales.remove(tmp) 
                return f"El empleado con cédula {cedula} ha sido eliminado."

        return f"No existe empleado con cédula {cedula}."




    
