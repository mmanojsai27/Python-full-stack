#Inheritance
'''
--->Inheritance is an OOP concept where one class (child/derived) acquired the properties and methods of another class (parent/

class parent:
   pass
class child(parent):
   pass

1) single inheritance
------------------------
A child class inherits from one parent is single inheritance
*Example:-
class animal:
    def sound(self):
        print('Animal makes sound')
class dog(animal):
    def barks(self):
        print("Dog barks")
d = dog()
d.sound()
d.barks()
---------------------------------------------
#Example:-
class father:
    def land(self):
        print('5 ar of land')
class son(father):
    def flat(self):
        print('3BHK flat')

s = son()
s.land()
s.flat()
-----------------------------------------------
2)Multiple Inheritance
----------------------
-->A child inherits more than one parent is called..
#Example:-
class father:
    def skills(self):
        print('Driving')
class mother:
    def talent(self):
        print("Cooking")
class sister:
    def learn(self):
        print('Python')
class son(father,mother):
    def mine(self):
        print('Coding')

all_ = son()
all_.talent()
all_.skills()
all_.mine()
--------------------------------------------
3) Multi-Level
----------------
#Example:-
class grandfather:
    def house(self):
        print('Own House')
class father(grandfather):
    def flat(self):
        print("New 3BHK flat")
class son(father):
    def car(self):
        print("Have a car")


_so = son()
_so.house()
_so.flat()

----------------------------------------------
4)Hierarchical
---------------
--> Multiple childs inherits from the same parent
#Example:-

class mother:
    def gold(self):
        print('10 KG Gold')
class pinky(mother):
    def show(self):
        print("Will get 5 KG Gold")
class yuktha(mother):
    def show_2(self):
        print("Remaining will get 5 KG Gold")


child_1 = pinky()
child_2 = yuktha()

child_1.gold()
child_1.show()

child_2.gold()
child_2.show_2()
-------------------------------------------------------
5)Hybrid Inheritance
--->This is the combination of two or more types of inheritance
Example of multiple + multi-level

class A:
    def methodA(self):
        print('Class A')
class B(A):
    def methodB(self):
        print('Class B')
class C(A):
    def methodC(self):
        print('Class C')
class D(B,C):
    def methodD(self):
        print('Class D')

so = D()
so.methodA()
so.methodB()
so.methodC()

-----------------------------------------------------------------------------------------
super()
--------
-->This super() function is used to access the parent class methods or constructor in the class......
1)Example:
class parent():
    def show(self):
        print('parent method')
class child(parent):
    def show(self):
        super().show()
        print('child class')

chi_ = child()
chi_.show()
---------------------------------------------
2)Example
class person:
    def __init__(self,name):
        self.name = name
class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
    def display(self):
        print(self.name)
        print(self.roll)

an = student('Manoj',777)
an.display()
--------------------------------------------------
'''


