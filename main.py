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
microodasB = Object("Microondas B", 0.0424, 308.66)
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

class Population:
    def __init__(self, numOfObjectsInObjectList, numberOfIndividualsPerPopulation):
        self.__individualList = []
        self.__numberOfObjects = numOfObjectsInObjectList
        self.__betterIndividual = None

    def __generateIndividual(self):
        individual = []
        for i in range(self.__numberOfObjects):
            randomGene = random.randint(0, 1)
            individual.append(randomGene)
        return individual

    def generateInitialPopulation(self):
        for i in range(numberOfIndividualsPerPopulation):
            individualGenerated = self.__generateIndividual()
            self.__individualList.append({"individual": individualGenerated, "fitnessValue": None})

    def evaluatePopulation(self):
        for i in range(len(self.__individualList)):
            individual = self.__individualList[i]["individual"]
            fitnessValue = fitness(individual)
            self.__individualList[i]["fitnessValue"] = fitnessValue

    def getPopulation(self):
        return self.__individualList
    
    def printPopulation(self):
        numberOfIndividual = len(self.__individualList)
        for i in range(numberOfIndividual):
            print(self.__individualList[i])
        print("\nQuantidade de Indivíduos: ", numberOfIndividual)

    def setNewPopulation(self, newGeneration):
        self.__individualList = newGeneration

    def mutarPopulation(self, mutationRate):
        for individuo in self.__individualList:
            if random.random() <= mutationRate:
                self.__mutarIndividuo(individuo)

    def __mutarIndividuo(self, individuo):
        gene_index = random.randint(0, len(individuo) - 1)
        novo_valor = random.randint(0, 1)
        individuo[gene_index] = novo_valor

    def saveBetterIndividual(self):
        betterIndividual = sorted(self.__individualList, key=lambda x: x["fitnessValue"], reverse=True)
        if self.__betterIndividual is None or betterIndividual[0]["fitnessValue"] > self.__betterIndividual["fitnessValue"]:
            self.__betterIndividual = betterIndividual[0]

    
    def getBetterIndividual(self):
        return self.__betterIndividual

class Crossover:
    def __init__(self, population):
        self.__numOfParents = int(len(population) / 2)
        self.__population = population
        self.__newGeneration = []

    def executeCrossover(self):
        parents = self.__getBetterParents()
        offspring = self.__begetChildren(parents)
        self.__newGeneration = offspring + parents

    def __getBetterParents(self):
        betterIndividual = sorted(self.__population, key=lambda x: x["fitnessValue"], reverse=True)
        return betterIndividual[:self.__numOfParents]


    def __begetChildren(self, parents):
        couples = self.__formCouples(parents)
        sizeOfIndividual = len(parents[0]["individual"])  

        offspring = []

        for couple in couples:
            sonOne = []
            sonTwo = []

            ponto_corte = random.randint(0, sizeOfIndividual)

            sonOne.extend(couple[0]["individual"][:ponto_corte])  # Primeira parte do pai para o filho 1
            sonOne.extend(couple[1]["individual"][ponto_corte:])  # Segunda parte da mãe para o filho 1

            sonTwo.extend(couple[1]["individual"][:ponto_corte])  # Primeira parte da mãe para o filho 2
            sonTwo.extend(couple[0]["individual"][ponto_corte:])  # Segunda parte do pai para o filho 2

            offspring.append({"individual": sonOne, "fitnessValue": None})
            offspring.append({"individual": sonTwo, "fitnessValue": None})

        return offspring
        

    def __formCouples(self, parentsList):
        parents = parentsList[:]
        Couples = []
        while len(parents) >= 2:
            idFatherOne = random.randint(0, len(parents)-1)
            fatherOne = parents[idFatherOne]
            parents.pop(idFatherOne)

            idFatherTwo = random.randint(0, len(parents)-1)
            fatherTwo = parents[idFatherTwo]
            parents.pop(idFatherTwo)

            Couples.append((fatherOne, fatherTwo))

        # Estava me perguntando como proceder se a lista de pais for impar, como formar casais? sempre sobra 1, o que fazer com esse 1
        # mudar as classes de arquivo

        return Couples
    
    def __justList(offspring, parents):
        NotImplemented

    def getNewGeneration(self):
        return self.__newGeneration

numOfObjectsInObjectList = 14
numberOfIndividualsPerPopulation = 24
mutationRate = 0.6

population = Population(numOfObjectsInObjectList, numberOfIndividualsPerPopulation)
population.generateInitialPopulation()
population.evaluatePopulation()
for i in range(10000):
    crossover = Crossover(population.getPopulation())
    crossover.executeCrossover()
    population.setNewPopulation(crossover.getNewGeneration())
    #population.mutarPopulation(mutationRate)
    population.evaluatePopulation()
    #population.saveBetterIndividual()


population.printPopulation()
#print("\n\nMelhor Individuo: ", population.getBetterIndividual())
