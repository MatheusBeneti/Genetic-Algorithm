class Object:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

class ObjectList:
    def __init__(self):
        self.list = []
        self.__numberOfObjectsInList = 0
    
    def addObject(self, obj):
        self.list.append(obj)
        self.__numberOfObjectsInList += 1
    
    def getNumberOfObjectsInList(self):
        return self.__numberOfObjectsInList