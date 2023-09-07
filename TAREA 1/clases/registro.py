from clases.usuario import Usuario
from clases.fecha import Fecha

class Registro :
    def __init__(self, capacidad) -> None:
        self.capacidad = capacidad
        self.contador = 0
        self.usuarios = [None] * capacidad

    # METHODS
    def buscarUsuario(self, id) :
        # Buscar en las entradas que si contengan usuarios
        for user in self.usuarios :
            if user != None :
                if user.getId() == id : return user
        return None
    
    def buscarPosicion(self, index) :
        # Buscar en las entradas que si contengan usuarios
        if self.usuarios[index] is not None : return self.usuarios[index]
        return None

    def agregar(self, usuario: Usuario) :
        # Si el array está lleno, no agregar el nuevo usuario
        if self.contador == self.capacidad : return False
        # Evitar que hayan 2 usuarios con misma id
        if self.buscarUsuario(usuario.getId()) != None : return False

        self.contador += 1

        for i in range(len(self.usuarios)) :
            """a = usuario.getId()
            if self.usuarios[i] != None : b = self.usuarios[i].id
            else : b = False"""

            if self.usuarios[i] == None or usuario.getId() < self.usuarios[i].id :
                # Insertar el elemento
                temp = self.usuarios[i]
                self.usuarios[i] = usuario
                c = 0
                # Desplazar los elementos hacia el final de la lista
                while temp != None :
                    c += 1
                    if i + c == len(self.usuarios) : break
                    self.usuarios[i + c], temp = temp, self.usuarios[i + c]
                break

        return True

  
    def eliminar(self, id):
        for i in range(len(self.usuarios)):
            if self.usuarios[i] is not None:
                if self.usuarios[i].id == id:
                    self.usuarios[i] = None
                    self.contador -= 1

        for i in range(len(self.usuarios)):
            j=len(self.usuarios)-1
            if self.usuarios[i]==None:
                while i!=j:
                    temp=self.usuarios[i+1]
                    self.usuarios[i+1]=self.usuarios[i]
                    self.usuarios[i]=temp
                    i+=1

    def importar(self, nombre_archivo="TAREA 1/realizadoPorChatGPT.txt"):
        lista_info=[]
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()

        for linea in lineas:
            linea = linea.strip()
            valores = linea.split(',')
            lista_info.append(valores)
        
            if len(valores) == 7:
                id = int(valores[0])
                nombre = valores[1]
                fecha_nac = valores[2]
                fecha_nac = fecha_nac.split('/')
                fecha_nac = Fecha(fecha_nac[0], fecha_nac[1], fecha_nac[2])
                ciudad= valores[3]
                email = valores[6]
                telefono = valores[5]
                direccion = valores[4]
                usuario = Usuario(id,nombre,fecha_nac,ciudad,direccion,telefono, email )
                self.agregar(usuario)

    def tofile(self, nombre_archivo="TAREA 1/realizadoPorChatGPT(despues).txt"):
        with open(nombre_archivo, 'w') as archivo:
            for usuario in self.usuarios:
                if usuario is not None:
                    linea = f"{usuario.id},{usuario.nombre},{'/'.join([usuario.fechaNacimiento.getdd(), usuario.fechaNacimiento.getmm(), usuario.fechaNacimiento.getaa()])},{usuario.ciudadNacimiento},{usuario.direccion},{usuario.telefono},{usuario.email}\n"
                    archivo.write(linea)

    def print(self) :
        for user in self.usuarios :
            if user is not None :
                print(user.toString())
