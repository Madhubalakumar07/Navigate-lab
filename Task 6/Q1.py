class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.__balance = balance   
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Invalid withdrawal")

    def get_balance(self):
        return self.__balance


account = BankAccount(101, "Dhanu", 5000)

account.deposit(1000)
account.withdraw(2000)

print("Current Balance:", account.get_balance())
