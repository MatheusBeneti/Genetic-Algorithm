import random

class Population:
    def __init__(self, numberOfIndividualsPerPopulation, spaceAvailableForObjects, objectList):
        self.__individualList = []
        self.__numberOfObjects = objectList.getNumberOfObjectsInList()
        self.__betterIndividual = None
        self.__numberOfIndividualsPerPopulation = numberOfIndividualsPerPopulation
        self.__spaceAvailableForObjects = spaceAvailableForObjects
        self.__obj_list = objectList

    def generateInitialPopulation(self):
            for i in range(self.__numberOfIndividualsPerPopulation):
                individualGenerated = self.__generateIndividual()
                self.__individualList.append({"individual": individualGenerated, "fitnessValue": None})

    def __generateIndividual(self):
        individual = []
        for i in range(self.__numberOfObjects):
            randomGene = random.randint(0, 1)
            individual.append(randomGene)
        return individual

    def evaluatePopulation(self):
        for i in range(len(self.__individualList)):
            individual = self.__individualList[i]["individual"]
            fitnessValue = self.__fitness(individual)
            self.__individualList[i]["fitnessValue"] = fitnessValue

    def __fitness(self, individual):
        fitnessValue = 0
        total_size = 0

        for i in range(len(individual)):
            if individual[i] == 1:
                fitnessValue += self.__obj_list.list[i].price
                total_size += self.__obj_list.list[i].size

        if total_size > self.__spaceAvailableForObjects:
            fitnessValue = 0
        return fitnessValue

    def getPopulation(self):
        return self.__individualList
    
    def printPopulation(self):
        numberOfIndividual = len(self.__individualList)
        for i in range(numberOfIndividual):
            print(self.__individualList[i])
        print("\nQuantidade de Indivíduos: ", numberOfIndividual)

    def setNewPopulation(self, newGeneration):
        self.__individualList = newGeneration

    def mutatePopulation(self, mutationRate):
        for individuo in self.__individualList:
            if random.random() <= mutationRate:
                self.__mutateIndividuo(individuo)

    def __mutateIndividuo(self, individuo):
        gene_index = random.randint(0, len(individuo["individual"]) - 1)
        novo_valor = random.randint(0, 1)
        individuo["individual"][gene_index] = novo_valor

    def saveBetterIndividual(self):
        best_individuals = sorted(self.__individualList, key=lambda x: x["fitnessValue"], reverse=True)
        found_better_individual = False

        for i in range(len(best_individuals)):
            nominee_for_best_individual = best_individuals[i]
            nominee_size = self.__getTheTotalweightOfTheIndividual(nominee_for_best_individual)

            if (self.__betterIndividual is None or
                (best_individuals[i]["fitnessValue"] > self.__betterIndividual["fitnessValue"] and
                nominee_size <= self.__spaceAvailableForObjects)):

                self.__betterIndividual = nominee_for_best_individual

                if nominee_size <= self.__spaceAvailableForObjects:
                    self.__betterIndividual["size"] = nominee_size
                    found_better_individual = True
                    break

            elif best_individuals[i]["fitnessValue"] > self.__betterIndividual["fitnessValue"]:
                break

        if found_better_individual:
            return


    def __getTheTotalweightOfTheIndividual(self, individual):
        totalSize = 0
        for i in range(len(individual["individual"])):
            if individual["individual"][i] == 1:
                totalSize += self.__obj_list.list[i].size
        return totalSize

    
    def getBetterIndividual(self):
        return self.__betterIndividual
    
    def printBetterCombination(self):
        for i, gene in enumerate(self.__betterIndividual["individual"]):
            if gene == 1:
                print(self.__obj_list.list[i].name)
        print("\n----------")