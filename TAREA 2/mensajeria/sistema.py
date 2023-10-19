from mensajeria.empleado import Empleado
from mensajeria.administrador import Administrador
from mensajeria.contacto import Contacto
from clases.listaSimple import ListaSimple

class Sistema :
    def __init__(self) -> None:
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
            self.credenciales.addLast(e)

    def exportarEmpleados(self, nombreArchivoA="Empleados.txt", nombreArchivoB="Password.txt") :
        with open(nombreArchivoA, "w") as file :
            for e in self.credenciales.toList() :
                file.write(f"{e.nombre} {e.cedula} {e.fechaNacimiento} {e.ciudadNacimiento} {e.contacto.telefono} {e.contacto.email} {e.contacto.direccion}\n")

        with open(nombreArchivoB, "w") as file :
            for e in self.credenciales.toList() :
                if isinstance(e, Administrador) :
                    rol = "administrador"
                else :
                    rol = "empleado"
                file.write(f"{e.cedula} {e.contraseña} {rol}\n")

    def login(self) -> Empleado :
        print("LOGIN")
        while True :
            cedula = input("Cedula: ")
            password = input("Contraseña: ")
            
            # Search user
            user = None
            tmp = self.credenciales.head
            while True :
                if tmp.getData().cedula == cedula :
                    user = tmp
                    break
                if tmp.getNext() == None : break
                tmp = tmp.getNext()
            if user == None : 
                print("Usuario y/o contraseña incorrecta")
                continue

            # Verify password
            if user.getData().contraseña != password :
                print("Usuario y/o contraseña incorrecta")
                continue
            
            return user.getData()
    
    def empleadoPorID(self, id) :
        tmp = self.credenciales.head
        while True :
            if tmp.getData().cedula == id : return tmp.getData()
            if tmp.getNext() == None : break
            tmp = tmp.getNext()
        return None
