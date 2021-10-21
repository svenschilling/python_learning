from typing import ClassVar


class dog:
    
    def __init__(self, petname, dograce, dogage):
        self.name = petname
        self.race = dograce
        self.age = dogage
        

    def status(self):
        print("Name: " + self.name)
        print("Race: " + self.race)
        print("Age: " + str(self.age))
        pass
"""
    def setDogAge (self, dogage):
        self.age = dogage
        pass

    def setDogRace (self, dograce):
        self.race = dograce
        pass
    
    def setPetname (self, petname):
        self.name = petname
        pass

    def bark(self):
        print("woof woof")
        pass
"""
test = dog("chuchu","dobermann",11)
test.status()

