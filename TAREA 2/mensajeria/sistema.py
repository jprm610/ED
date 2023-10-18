from mensajeria.empleado import Empleado
from mensajeria.administrador import Administrador
from mensajeria.contacto import Contacto
from clases.listaSimple import ListaSimple

class Sistema :
    def __init__(self) -> None:
        self.empleados = ListaSimple()
        self.credenciales = ListaSimple()

    def importarEmpleados(self, nombreArchivoA="Empleados.txt", nombreArchivoB="Password.txt") :
        with open(nombreArchivoA, "r") as file :
            linesA = file.readlines()

        with open(nombreArchivoB, "r") as file :
            linesB = file.readlines()

        lines = []
        for a, b in zip(linesB, linesA) :
            a, b = a.strip(), b.strip()
            lines.append(f"{a} {b}")

        for line in lines :
            line = line.strip()
            values = line.split(' ')
            
            cc = values[0]
            password = values[1]
            rol = values[2]
            nombre = values[3]
            fechaNac = values[5:8]
            ciudadNac = values[8]
            celular = values[9]
            email = values[10]
            direccion = values[13:]

            if rol == "empleado" :
                e = Empleado(nombre, cc, password, fechaNac, ciudadNac, Contacto(celular, email, direccion))
            else :
                e = Administrador(nombre, cc, password, fechaNac, ciudadNac, Contacto(celular, email, direccion))
            self.empleados.addLast(e)
