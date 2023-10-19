from mensajeria.contacto import Contacto
from mensajeria.mensaje import Mensaje

class Empleado :
    def __init__(self, nombre, cedula, contraseña, fechaNacimiento, ciudadNacimiento, contacto:Contacto) -> None:
        self.nombre = nombre
        self.cedula = cedula
        self.contraseña = contraseña
        self.fechaNacimiento = fechaNacimiento
        self.ciudadNacimiento = ciudadNacimiento
        self.contacto = contacto
        self.mensajes = [Mensaje]

    def importarMensajes(self, nombreArchivo="Mensajes.txt") :
        with open(nombreArchivo, "r") as file :
            lines = file.readlines()

        for line in lines :
            line = line.strip()
            values = line.split(', ')
            remitente = values[0]
            destinatario = values[1]
            time = values[2]
            asunto = values[3]
            texto = values[4]
            bandeja = values[5]

            if remitente == self.nombre or destinatario == self.nombre :
                m = Mensaje(remitente, destinatario, time, asunto, texto, bandeja)
                self.mensajes.append(m)

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
