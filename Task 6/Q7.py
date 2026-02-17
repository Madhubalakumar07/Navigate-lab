class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def update_salary(self, amount):
        if amount > 0:
            self.__salary = amount

    def get_salary(self):
        return self.__salary
