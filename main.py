import random

class Object:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

RefrigeratorA = Object("Refrigerator A", 0.751, 999.90)
celular = Object("Celular", 0.00000899, 2199.12)
tv55 = Object("TV 55", 0.400, 4346.99)
tv50 = Object("TV 50", 0.290, 3999.90)
tv42 = Object("TV 42", 0.200, 2999.90)
notebookA = Object("Notebook A", 0.00350, 2499.90)
ventilador = Object("Ventilador", 0.496, 199.90)
microodasA = Object("Microondas A", 0.0424, 308.66)
microodasB = Object("Microondas A", 0.0424, 308.66)
microodasC = Object("Microondas C", 0.0319, 299.29)
refrigeradorB = Object("Refrigerador B", 0.635, 849.00)
refrigeradorC = Object("Refrigerador C", 0.870, 1199.89)
notebookB = Object("Notebook B", 0.498, 1999.90)
notebookC = Object("Notebook C", 0.527, 3999.00)

class ObjectList:
    def __init__(self):
        self.list = []
    
    def addObject(self, obj):
        self.list.append(obj)

obj_list = ObjectList()
obj_list.addObject(RefrigeratorA)
obj_list.addObject(celular)
obj_list.addObject(tv55)
obj_list.addObject(tv50)
obj_list.addObject(tv42)
obj_list.addObject(notebookA)
obj_list.addObject(ventilador)
obj_list.addObject(microodasA)
obj_list.addObject(microodasB)
obj_list.addObject(microodasC)
obj_list.addObject(refrigeradorB)
obj_list.addObject(refrigeradorC)
obj_list.addObject(notebookB)
obj_list.addObject(notebookC)

spaceAvailableForObjects = 3.0
penalty = 1.0

def fitness(combinationOfObjects):
    fitnessValue = 0
    total_size = 0

    for i in range(len(combinationOfObjects)):
        if combinationOfObjects[i] == 1:
            fitnessValue += obj_list.list[i].price
            total_size += obj_list.list[i].size

    if total_size > spaceAvailableForObjects:
        fitnessValue -= penalty * (total_size - spaceAvailableForObjects)

    return fitnessValue

# Exemplo de uso:

class Population:
    def __init__(self,numOfObjectsInObjectList, numberOfIndividualsPerPopulation):
        self.__individualList = []
        self.__numberOfObjects = numOfObjectsInObjectList

    def __generateIndividual(self):
        individual = []
        for i in range(self.__numberOfObjects):
            randomGene = random.randint(0, 1)
            individual.append(randomGene)
        return individual
    
    def generateInitialPopulation(self):
        for i in range(numberOfIndividualsPerPopulation):
            individualGenerated = self.__generateIndividual()
            self.__individualList.append(individualGenerated)
    
    def evaluatePopulation(self):
        for i in range(len(self.__individualList)):
            fitnessValue = fitness(self.__individualList[i])
            self.__individualList[i] = (self.__individualList[i], fitnessValue)

    def getPopulationList(self):
        return self.__individualList

numOfObjectsInObjectList = 14
numberOfIndividualsPerPopulation = 6

population = Population(numOfObjectsInObjectList, numberOfIndividualsPerPopulation)
population.generateInitialPopulation()
population.evaluatePopulation()

print(population.getPopulationList())

combination = [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1]
result = fitness(combination)
print(result)

