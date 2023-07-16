
#----------------------------------------------------------------
# primeiro criar a estrutura para representar as pessoas ou cidades 
# A lista ira conter as cidade e a sigla do aeroporto
flightsDataPath = 'flights.txt'
people = ['Paris','Berlin']
flights = []



class Person:
    def __init__(self, name, cityOfOrigin, destinationCity):
        self.name = name
        self.cityOfOrigin = cityOfOrigin
        self.destinationCity = destinationCity
        self.availableFlights = []  
        

    def createBetterPackage():
        print("NotImplemented")

    def searchAvailableFlights(self, flightsDataPath):
        with open(flightsDataPath, 'r') as file:
            for line in file:
                first_word = line.split(',')[0].strip()
                second_word = line.split(',')[1].strip()
                if first_word == self.cityOfOrigin and second_word == self.destinationCity:
                    self.availableFlights.append(line)
                
                if first_word == self.destinationCity and second_word == self.cityOfOrigin:
                    self.availableFlights.append(line)
                    
    def printAvailableFlights(self):
        print(self.availableFlights)


# Primeiro voo de Paris para Roma e o primeiro voo do dia de Roma para Paris 
firstPerson = Person('alice', 'Berlim', 'Roma')
firstPerson.searchAvailableFlights(flightsDataPath)
firstPerson.printAvailableFlights()
