from mensajeria.contacto import Contacto

class Empleado :
    def __init__(self, nombre, cedula, contraseña, fechaNacimiento, ciudadNacimiento, contacto:Contacto) -> None:
        self.nombre = nombre
        self.cedula = cedula
        self.contraseña = contraseña
        self.fechaNacimiento = fechaNacimiento
        self.ciudadNacimiento = ciudadNacimiento
        self.contacto = contacto

    def bandejaEntrada(self) :
        pass

    def mensajesLeidos(self) :
        pass

    def borradores(self) :
        pass

    def redactarMensaje(self) :
        pass

    def toString(self) :
        return f"{self.nombre} {self.cedula}"
