class Employee:
    def calculate_salary(self): pass

class FullTime(Employee):
    def calculate_salary(self): return 50000

class Contract(Employee):
    def calculate_salary(self): return 30000
