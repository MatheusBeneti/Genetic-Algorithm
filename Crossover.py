import random

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

    def getNewGeneration(self):
        return self.__newGeneration