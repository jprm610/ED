class BSTEntry:
    def __init__(self, e, key):
        self.data = e
        self.key = key

    def getData(self):
        return self.data
    
    def getKey(self):
        return self.key
    
    def setData(self, d):
        self.data = d

    def setKey(self, key):
        self.key = key
    def __str__(self):
        return f"BSTEntry con data: {self.data}, key: {self.key}"
        