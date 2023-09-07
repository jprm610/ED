class Direccion :
    def __init__(self, calle, noCalle, nomenclatura, barrio, ciudad) -> None:
        self.calle = calle
        self.noCalle = noCalle
        self.nomenclatura = nomenclatura
        self.barrio = barrio
        self.ciudad = ciudad

    def toString(self) :
        return f"{self.calle} {self.noCalle} {self.nomenclatura} {self.barrio} {self.ciudad}"

    # GETTERS
    def getCalle(self) :
        return self.calle
    
    def getNoCalle(self) :
        return self.noCalle
    
    def getNomenclatura(self) :
        return self.nomenclatura
    
    def getBarrio(self) :
        return self.barrio
    
    def getCiudad(self) :
        return self.ciudad
