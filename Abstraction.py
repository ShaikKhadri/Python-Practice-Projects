from abc import ABC, abstractmethod
#
class Whatsapp(ABC):
    @abstractmethod
    def send(self):
        pass

class SendPhoto(Whatsapp):
    def send(self):
        print("Compression the photo...")
        print("Encrypting photo..")
        print("Sending the photo...")
        print("Decrypting the photo...")
        print("Photo sent!")

class SendText(Whatsapp):
    def send(self):
        print("Checking character limit")
        print("Encrypting message..")
        print("Sending the message...")
        print("Decrypting message...")
        print("Message sent!")
a1=SendPhoto()
a2=SendText()
a2.send()
a1.send()
from abc import abstractmethod


# Design an abstract class PaymentGateway using ABC with abstract methods initiate(amount), verify(transaction_id), and refund(transaction_id). Create two concrete
# classes RazorpayGateway and PayPalGateway that inherit from PaymentGateway and implement all three methods. Create objects of both concrete classes
# and call their methods. Also verify that PaymentGateway cannot be instantiated directly.

# class PaymentGateway(ABC):
#     @abstractmethod
#     def initiate(self,amount):
#         pass
#     @abstractmethod
#     def verify(self,transaction_id):
#         pass
#     @abstractmethod
#     def refund(self,transaction_id):
#         pass
# class RazorpayGateway(PaymentGateway):
#     def initiate(self,amount):
#         print("RazorpayGateway initiate:",amount)
#     def verify(self,transaction_id):
#         print("RazorpayGateway verified:",transaction_id)
#     def refund(self,transaction_id):
#         print("RazorpayGateway refund:",transaction_id)
# class PayPalGateway(PaymentGateway):
#     def initiate(self,amount):
#         print("PayPalGateway initialize:",amount)
#     def verify(self,transaction_id):
#         print("PayPAlGateway verified:",transaction_id)
#     def refund(self,transaction_id):
#         print("PayPalGateway refund:",transaction_id)
#
# p1=RazorpayGateway()
# p1.initiate(1000)
# p1.verify(2000)
# p1.refund(500)
#
# r=PayPalGateway()
# r.initiate(101)
# r.verify(27)
# r.refund(90)

# Create an abstract class Animal(ABC) with abstract methods speak() and move(), and a concrete method breathe() shared by all.
# Implement Dog, Bird, and Fish. Prove that the contract is enforced by trying to instantiate Animal or a subclass that forgot to implement speak().
# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass
#     @abstractmethod
#     def move(self):
#         pass
#     def breathe(self):
#         print("Animal is breathing")
# class Dog(Animal):
#     def speak(self):
#         print("Dog can make sound")
#     def move(self):
#         print("Dog can move")
# class Bird(Animal):
#     def speak(self):
#         print("Bird say chirp")
#     def move(self):
#         print("Bird can fly")
# class Fish(Animal):
#     def speak(self):
#         print("Fish can blub")
#     def move(self):
#         print("fish can swim")
# d=Dog()
# d.speak()
# d.move()
# d.breathe()
# b=Bird()
# b.speak()
# b.move()
# b.breathe()
# f=Fish()
# f.speak()
# f.move()
# f.breathe()

# Create an abstract class DataStorage(ABC) with an abstract property storage_type and abstract methods save(data), load(key), and delete(key).
# Implement FileStorage and MemoryStorage. Demonstrate that both are interchangeable.
# class DataStorage(ABC):
#     @property
#     @abstractmethod
#     def storage_type(self):
#         pass
#     @abstractmethod
#     def save(self,data):
#         pass
#     @abstractmethod
#     def load(self,data):
#         pass
#     @abstractmethod
#     def delete(self,data):
#         pass
# class FileStorage(DataStorage):
#     @property
#     def storage_type(self):
#         return "File Storage"
#     def save(self,data):
#         print("Saving data to a file:",data)
#     def load(self,data):
#         print("loading data from file:",data)
#     def delete(self,data):
#         print("deleting data from file:",data)
# class MemoryStorage(DataStorage):
#     @property
#     def storage_type(self):
#         return "Memory storage"
#     def save(self,data):
#         print("saving data to a Memory:",data)
#     def load(self,data):
#         print("loading data from a Memory:",data)
#     def delete(self,data):
#         print("deleting data from a Memory:",data)
# f=FileStorage()
# print(f.storage_type)
# f.save("hello")
# f.load(20)
# f.delete(10)
# m=MemoryStorage()
# print(m.storage_type)
# m.save("King")
# m.load(200)
# m.delete(100)

# Explain in your own words: What is the difference between abstraction and encapsulation?
# Write one class example that demonstrates both concepts at the same time.