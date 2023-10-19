from mensajeria.contacto import Contacto
from mensajeria.empleado import Empleado

class Administrador(Empleado) :
    def __init__(self, nombre, cedula, contraseña, fechaNacimiento, ciudadNacimiento, contacto: Contacto) -> None:
        super().__init__(nombre, cedula, contraseña, fechaNacimiento, ciudadNacimiento, contacto)

    def agregarUsuario(self, sistema):
        nombre = input("Nombre: ")
        cedula = input("Cedula: ")
        contraseña = input("Contraseña: ")
        fechaNacimiento = input("Fecha de Nacimiento: ")
        ciudadNacimiento = input("Ciudad De Nacimiento: ")
        celular = input("Celular: ")
        email = input("Email: ")
        direccion = input("Direccion: ")
        nuevo_usuario = Empleado(nombre, cedula, contraseña, fechaNacimiento, ciudadNacimiento, Contacto(celular, email, direccion))
        sistema.credenciales.addLast(nuevo_usuario)
        return f"Usuario {nombre} ha sido agregado por el administrador {self.nombre}."

    def cambiarContraseña(self,empleado) :
        newPassword=input("Ingrese contraseña: ")
        empleado.contraseña=newPassword
        return empleado.contraseña

    def eliminarEmpleado(self, sistema):
        cedula = input("Cedula empleado a eliminar: ")
        empleado_borrar = None
        tmp = sistema.credenciales.head

        while tmp:
            if tmp.getData().cedula == cedula:
                empleado_borrar = tmp.getData()
                sistema.credenciales.remove(tmp) 
                return f"El empleado con cédula {cedula} ha sido eliminado."

        return f"No existe empleado con cédula {cedula}."




    
