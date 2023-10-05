class NodoSimple :
    def __init__(self, data:object) -> None:
        self.data = data
        self.next = None

    def getData(self) :
        return self.data
    
    def getNext(self) :
        return self.next
    
    def setData(self, data) :
        self.data = data

    def setNext(self, next) :
        self.next = next
    