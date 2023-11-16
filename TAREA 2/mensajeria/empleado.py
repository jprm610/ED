from mensajeria.contacto import Contacto
from mensajeria.mensaje import Mensaje
from mensajeria.bandejas.entrada import Entrada
from mensajeria.bandejas.leidos import Leido
from mensajeria.bandejas.borradores import Borradores
from mensajeria.bandejas.enviados import Enviados

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
        self.bandejaDeBorradores = Borradores()
        self.mensajesEnviados = Enviados()

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
            elif remitente == self.nombre and bandeja == 'B' :
                self.bandejaDeBorradores.agregar(Mensaje(remitente, destinatario, time, asunto, texto, bandeja))
            else :
                self.mensajesEnviados.agregar(Mensaje(remitente, destinatario, time, asunto, texto, bandeja))

    def exportarMensajes(self, nombreArchivo="Mensajes.txt") :
        mensajes = self.bandejaDeEntrada.toList() + self.bandejaDeLeidos.toList() + self.bandejaDeBorradores.toList() + self.mensajesEnviados.toList()
        with open(nombreArchivo, "w") as file :
            for m in mensajes :
                file.writelines(f"{m.toFile()}\n")

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
        while True :
            print("BANDEJA DE BORRADORES")
            self.bandejaDeBorradores.print()
            
            print("0. Volver")
            print("1. Enviar ultimo borrador")
            print("2. Descartar ultimo borrador")
            entrada = input("Seleccione lo que quiera hacer: ")
            if entrada == '1' :
                m = self.bandejaDeBorradores.pop()
                m.bandeja = "BA"
                self.mensajesEnviados.agregar(m)
            elif entrada == '2' :
                self.bandejaDeBorradores.pop()
            else : return

    def redactarMensaje(self, sistema) :
        from time import gmtime, strftime

        print("REDACTAR MENSAJE")
        cc = input('Ingrese la cedula del destinatario: ')

        destinatario = sistema.empleadoPorID(cc)
        time = strftime("%d/%m/%Y %H:%M", gmtime())
        asunto = input("Asunto: ")
        texto = input("Texto: ")
        print("0. Volver sin guardar")
        print("1. Enviar")
        print("2. Guardar como borrador")
        entrada = input("Seleccione lo que quiera hacer: ")
        if entrada == '1' :
            self.mensajesEnviados.agregar(Mensaje(self.nombre, destinatario.nombre, time, asunto, texto, "BA"))
        elif entrada == '2' :
            self.bandejaDeBorradores.agregar(Mensaje(self.nombre, destinatario.nombre, time, asunto, texto, "B"))
        else : return

    def toString(self) :
        return f"{self.nombre} {self.cedula}"
