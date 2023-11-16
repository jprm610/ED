class BSTEntry:
    def __init__(self, e, key):
        self.data = e
        self.key = self.calcKey(key)

    def getData(self):
        return self.data
    
    def getKey(self):
        return self.key
    
    def setData(self, d):
        self.data = d

    def setKey(self, key):
        self.key = key

    def calcKey(self, cedula) :
        string = str(cedula)
        s = 0
        for n in string :
            s += int(n)
        return s

    def __str__(self):
        return f"BSTEntry con data: {self.data}, key: {self.key}"
        