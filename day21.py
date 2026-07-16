#self keyword:-
'''
---self refers to current object....

class Test:
    def display(self):
        print(self)
te = Test()
print(te)
te.display()


Constructor
---------------
---> This constructor initializes the object automatically when it is created..... 

class batch:
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch
    def display(self):
        print(self.name)
        print(self.branch)
        
B4=batch('Manoj','CSE')
B4.display()
-------------------------------------------------
class fam:
    def __init__(self):
        self._name = "Manoj"

f = fam()
print(f._name)
--------------------------------------------
#Out Side the class
class bank:
    def __init__(self):
        self.__pin = '6600'
AC = bank()
print(AC._bank__pin)`
----------------------------------------------
#In Side the class
class Bank:
    def __init__(self):
        self.__pin = '7700'
    def __display(self):
        print(self.__pin)
ac=Bank()
ac.display()

------------------------------------------------
Encapsulation
--------------
--->Means wrapping the data and methods into a single unit(class) while controlling access to the data...

class atm:
    def __init__(self,balance):
        self._balance = balance
    def deposit(self,amount):
        self._balance += amount
        print(self._balance)
trans = atm(balance = int(input("Enter Amount: ")))
trans.deposit(amount = int(input("Enter Amount: ")))
'''


