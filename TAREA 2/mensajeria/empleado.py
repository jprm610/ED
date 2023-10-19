from mensajeria.contacto import Contacto
from mensajeria.mensaje import Mensaje
from mensajeria.bandejas.entrada import Entrada
from mensajeria.bandejas.leidos import Leido

class Empleado :
    def __init__(self, nombre, cedula, contraseña, fechaNacimiento, ciudadNacimiento, contacto:Contacto) -> None:
        self.nombre = nombre
        self.cedula = cedula
        self.contraseña = contraseña
        self.fechaNacimiento = fechaNacimiento
        self.ciudadNacimiento = ciudadNacimiento
        self.contacto = contacto
        self.bandejaDeEntrada = Entrada()
        self.bandejaDeLeidos = Leido()

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

            if destinatario == self.nombre and bandeja == "BA" :
                self.bandejaDeEntrada.addFirst(Mensaje(remitente, destinatario, time, asunto, texto, bandeja))
            elif destinatario == self.nombre and bandeja == "ML" :
                self.bandejaDeLeidos.add_mensaje(Mensaje(remitente, destinatario, time, asunto, texto, bandeja))

    def bandejaEntrada(self) :
        while True :
            print("BANDEJA DE ENTRADA")
            self.bandejaDeEntrada.print()
            entrada = input("Seleccione un mensaje para leer o 0 para regresar: ")
            if entrada == '0' : return

            mensajeParaLeer = self.bandejaDeEntrada.get(int(entrada) - 1)
            print(mensajeParaLeer.toString(False))
            mensajeParaLeer.bandeja = "ML"
            self.bandejaDeLeidos.add_mensaje(mensajeParaLeer)
            self.bandejaDeEntrada.remove(mensajeParaLeer)
            input("Presione cualquier tecla para regresar a la bandeja de entrada: ")

    def mensajesLeidos(self) :
        while True :
            print("BANDEJA DE MENSAJES LEIDOS")
            self.bandejaDeLeidos.print()
            entrada = input("Seleccione un mensaje para leer o 0 para regresar: ")
            if entrada == '0' : return

            mensajeParaLeer = self.bandejaDeLeidos.get(int(entrada) - 1)
            print(mensajeParaLeer.toString(False))
            input("Presione cualquier tecla para regresar a la bandeja de entrada: ")

    def borradores(self) :
        pass

    def redactarMensaje(self) :
        pass

    def toString(self) :
        return f"{self.nombre} {self.cedula}"
