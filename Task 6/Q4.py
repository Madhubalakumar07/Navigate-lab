class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def study(self): print("Studying")

class Teacher(Person):
    def teach(self): print("Teaching")
