
from Crossover import *
from Object import *
from Population import *

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


def fitness(combinationOfObjects):
    fitnessValue = 0
    total_size = 0

    for i in range(len(combinationOfObjects)):
        if combinationOfObjects[i] == 1:
            fitnessValue += obj_list.list[i].price
            total_size += obj_list.list[i].size

    if total_size > spaceAvailableForObjects:
        fitnessValue = 0
    return fitnessValue


spaceAvailableForObjects = 3.0
numberOfIndividualsPerPopulation = 48
mutationRate = 0.1
NumberOfGenerations = 1000


population = Population(numberOfIndividualsPerPopulation, spaceAvailableForObjects, obj_list)

population.generateInitialPopulation()
population.evaluatePopulation()

for i in range(NumberOfGenerations):
    crossover = Crossover(population.getPopulation())
    crossover.executeCrossover()
    population.setNewPopulation(crossover.getNewGeneration())
    population.mutarPopulation(mutationRate) 
    population.evaluatePopulation()
    population.saveBetterIndividual()

population.printPopulation()
print("\nMelhor Indivíduo: ", population.getBetterIndividual(),"\n\n\n")
