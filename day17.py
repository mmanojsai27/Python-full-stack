#Modules
'''-------------
--> A module is a python file (.py) that contains reusable code

1)Variable
2)Functions
3)Classes
4)Objects
5)Statements

Q)Why This?
a)Insead of writing the same code repeatedly, we can store it in a module and use it whenever needed.......

Types of module
------------------
1.user-defined
**import specific function

import first_module
print(first_module.div(8,2))


from first_module import *
print(add(3,3))
print(sub(5,3))

import first_module as m
print(m.sqr(2,4))

2.Built-in
-----------
-math
------
Example:-
import math
print(math.sqrt(25))
print(math.factorial(5))
print(math.pow(2,5))
print(math.pi)

------------------------------------------
ii)os()
-->The os module is used to interact with operating system
import os
print(os.getcwd())
os.mkdir("SAI")
os.rmdir("SAI")


iii)sys
---------
-->This will provide the information about python interpeter
import sys
print(sys.version)

iv)random
-------------
Used to generate random values
->
import random
print(random.randint(1000,9999))

colors = ('Yellow','Red','Blue','Green','Black')
print(random.choice(colors))

'''


















