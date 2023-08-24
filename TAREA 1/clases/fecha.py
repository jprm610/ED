class Fecha :
    def __init__(self, dd, mm, aa) -> None:
        self.dd = dd
        self.mm = mm
        self.aa = aa

    def toString(self) :
        return f"{self.dd}/{self.mm}/{self.aa}" 

    # GETTERS AND SETTERS
    def getdd(self) :
        return self.dd
    
    def getmm(self) :
        return self.mm
    
    def getaa(self) :
        return self.aa
    
    def setdd(self, d) :
        self.dd = d

    def setmm(self, m) :
        self.mm = m

    def setaa(self, a) :
        self.aa = a
