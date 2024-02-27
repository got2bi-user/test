from abc import ABC, abstractmethod
class Flying(ABC):
    @abstractmethod
    def fly(self):
        pass
class Floating(ABC):
    @abstractmethod
    def swim(self):
        pass
class Running(ABC):
    @abstractmethod
    def run(self):
        pass
class Animal(ABC):
    pass

class Ostrich(Animal, Running):
    def run(self):
        print("Ostrich is running")
class Hippo(Animal, Floating, Running):
    def swim(self):
        print("Hippo is floating")
    def run(self):
        print("Hippo is running")
class Parrot(Animal, Flying):
    def fly(self):
        print("Parrot is flying")
class Shark(Animal, Floating):
    def swim(self):
        print("Shark is floating")


ostrich = Ostrich()
hippo = Hippo()
parrot = Parrot()
shark = Shark()

AnimalList = []
AnimalList.append(ostrich)
AnimalList.append(hippo)
AnimalList.append(parrot)
AnimalList.append(shark)

AnimalListRunning = []

for Anim in AnimalList:
    try:
        Anim.fly()
    except:
        pass
    try:
        Anim.run()
        AnimalListRunning.append(Anim)
    except:
        pass
    try:
        Anim.swim()
    except:
        pass

print(AnimalListRunning)