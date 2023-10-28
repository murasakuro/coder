#Crea una herencia múltiple, trabajando con Mamífero, Cetáceo, AnimalMarino. 
class Mammal:
    def __init__(self,mammaryGlands,lifeExpectancy):
        self.breasts=mammaryGlands
        self.lifeExpectancy=lifeExpectancy
    def suckle(self):
        print("Chuu chuu")
    def birth(self):
        print("yippee! im born!")
class MarineAnimal:
    def __init__(self,hasGills,species):
        self.hasGills=hasGills
        self.species=species
    def swim(self):
        print("swish swish")
class Cetacean(Mammal,MarineAnimal):
    def __init__(self,mammaryGlands,lifeExpectancy,hasGills,species,notes,livesIn,weight):
        super().__init__(mammaryGlands,lifeExpectancy)
        super().__init__(hasGills,species)
        self.notes=notes
        self.livesIn=livesIn
        self.weight=weight

orca=Cetacean(True,"50-90 years",False,"Orca","Biggest delfinids.","All oceans","2600-9000kg")
cachalote=Cetacean(True,"70 years",False,"Sperm Whale","Biggest odontocets.","All deep oceans between the pack ice of the artic and antartic.","13000-14000kg")

orca.swim()
orca.suckle()
orca.birth()