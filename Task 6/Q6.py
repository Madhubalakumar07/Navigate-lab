class Notification:
    def send(self, msg): pass

class Email(Notification):
    def send(self, msg): print("Email:", msg)

class SMS(Notification):
    def send(self, msg): print("SMS:", msg)
