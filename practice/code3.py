from abc import ABC, abstractmethod
class notification(ABC):
    @abstractmethod
    def send(self,msg):
        pass
class email(notification):
    def send(self,msg):
        return f"The message is {msg}"
class sms(notification):
    def send(self,msg):
        return f"The message is {msg}"
notify1 = email()
notify2 = sms()
print(notify1.send("Iam the danger"))
print(notify2.send("iam the one who knoks"))