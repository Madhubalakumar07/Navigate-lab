class Payment:
    def pay(self, amount): pass

class Card(Payment):
    def pay(self, amount): print("Paid via Card:", amount)

class UPI(Payment):
    def pay(self, amount): print("Paid via UPI:", amount)
