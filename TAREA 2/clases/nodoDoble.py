class NodoDoble :
    def __init__(self, e:object) -> None:
        self.data = e
        self.prev = None
        self.next = None

    def getData(self) :
        return self.data
    
    def getPrev(self) :
        return self.prev
    
    def getNext(self) :
        return self.next
    
    def setData(self, data:object) :
        self.data = data
    
    def setPrev(self, prev) :
        self.prev = prev

    def setNext(self, next) :
        self.next = next