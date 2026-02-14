from abc import ABC,abstractmethod
class engine(ABC):
    @abstractmethod
    def start(self):
        print("hey rider")
class car(engine):
    def start(self):
        return "Its a v12 engine"
class bike(engine):
    def start(self):
        return "It is a 650cc twin cylinder engine"
m5 = car()
gt = bike()
print(m5.start())
print(gt.start())