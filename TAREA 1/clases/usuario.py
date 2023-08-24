class Usuario :
    def __init__(self, id, nombre, fechaNacimiento=None, ciudadNacimiento=None, direccion=None, telefono=None, email=None) -> None:
        self.id = id
        self.nombre = nombre
        self.fechaNacimiento = fechaNacimiento
        self.ciudadNacimiento = ciudadNacimiento
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    def toString(self) :
        return f"{self.id} {self.nombre}"

    # GETTERS AND SETTERS
    def getId(self) :
        return self.id
    
    def getNombre(self) :
        return self.nombre
    
    def getFechaNacimiento(self) :
        return self.fechaNacimiento
    
    def getCiudadNacimiento(self) :
        return self.ciudadNacimiento
    
    def getDireccion(self) :
        return self.direccion
    
    def getTelefono(self) :
        return self.telefono
    
    def getEmail(self) :
        return self.email
    
    def setId(self, id) :
        self.id = id

    def setNombre(self, nombre) :
        self.nombre = nombre

    def setFechaNacimiento(self, fechaNacimiento) :
        self.fechaNacimiento = fechaNacimiento

    def setCiudadNacimiento(self, ciudadNacimiento) :
        self.ciudadNacimiento = ciudadNacimiento

    def setDireccion(self, direccion) :
        self.direccion = direccion

    def setTelefono(self, telefono) :
        self.telefono = telefono

    def setEmail(self, email) :
        self.email = email
