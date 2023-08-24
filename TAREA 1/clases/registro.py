from clases.usuario import Usuario

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
    
    def buscarPosicion(self, id) :
        # Buscar en las entradas que si contengan usuarios
        for i in range(len(self.usuarios)) :
            if self.usuarios[i] != None :
                if self.usuarios[i].getId() == id : return i
        return None

    def agregar(self, usuario: Usuario) :
        # Si el array está lleno, no agregar el nuevo usuario
        if self.contador == self.capacidad : return False
        # Evitar que hayan 2 usuarios con misma id
        if self.buscarUsuario(usuario.getId()) != None : return False

        self.contador += 1

        for i in range(len(self.usuarios)) :
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

    def eliminar(self, id) :
        posicionUsuarioAEliminar = self.buscarPosicion(id)
        if posicionUsuarioAEliminar == None : return False

        
