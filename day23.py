#Ploymorphism
'''
-----------------------
--> Ploymorphism means many forms
--> It allows same method, function or operator to perform different tasks depending on the same object...

Types:-
-------
1)Method Overloading
---------------------
--> Method Overloading means having multiple methods with the same name but different parameters...
#Example:-
class Cal:
    def add(self,num,num_2 = 3):
        print(num + num_2)
    def add(self,num=0,num_2=0,num_3=0):
        print(num+num_2+num_3)
obj = Cal()
obj.add(7,8)
obj.add(27,31,4)

2)Method Overriding
--------------------
--> The method overriding occurs when a child class provides its own implementation of a method already defined in its parent class..

class animal:
    def sound(self):
        print("Animal make sounds")
class dog(animal):
    def sound(self):
        print("Dogs barks")

d=dog()
d.sound()

3)Operator Overloading
--> This allows operators (+,-,*) to work differently for user-defined objects.
1.__add__ (+)
2.__sub__ (-)
3.__Mul__ (*)
4.__truediv__(/)
5.__eq__ (==)
6.__It__ (<)

#Example:
class student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return self.marks - other.marks
s1 = student(27)
s2 = student(31)
print(s1 + s2)
'''
#DATA Abstraction:
'''
--> Data Abstraction is the process of hiding implementation details and showing only the essentail data to the user..
-----------
Example:-
---------
-ATM
-CAR
-APP

from abc import ABC, abstractmethod

class parent:

    @abstractmethod
    def display(self):
        pass
#Example:--
from abc import ABC, abstractmethod

class bank:
    @abstractmethod
    def interest(self):
        raise NotImplementError('Subclass must implement interest()')

class SBI(bank):
    def interest(self):
        print("SBI interest Rate: 6.7%")

class HDFC(bank):
    def interest(self):
        print("HDFC interest Rate: 5.5%")

class ICIC(bank):
    def interest(self):
        print("ICIC interest Rate: 6.9%")

Banks = [SBI(),HDFC(),ICIC()]

for j in Banks:
    j.interest()
'''

    
    
