#Functions
'''
---> Function us a block of code that can be Resuable...
---> Function can avoid the repeated line of code....

Functions are 2 Types
----------------------
1)built-in function
-------------------
eg--> print(), max(), type(), min(), sum()

2)User -define
---------------
--->This funtion starts with a keyword (def)

def func_name(parameters):
    ----------
    ----------
    ----------
func_name(arugments)
*Example:
-->
def add(a,b):
    print(a + b)
add(3,7)

Types of Arugments()
---------------------
1)Requered Arugmnets
---------------------
--->We have to pass same number arugments with defination of the function.
Example-->
def add(a,b):
    print(a)
add(2)

2)Default
---------------
--->
--->Example:
def add(a,b):
    print(a)
add(b = 7 , a = 31)
*
Example 2
-->
num = 7
num_2 = 27
num_3 = 31
def add(a,b,c):
    print(a)
    print(c)
    print(b)
add(num,num_3,num_2)



3)Keyword
--------------------------------------------------------------------------------------
--->We can pass as a pair Like (Variable = datatype)
def add(a,b):
    print(a + b)
add(a="Man",b = "OJ")

4)Variable lenght
------------------------------------------------------------------------
--->Example for (*Argrs) WE use Single star for Tuplees.
num = 7
num_2 = 27
num_3 = 31
num4 = "Python"
def add(*a):
    print(a)
add(num,num_3,num_2,num4)

**Example--->(**asterisk)We Use Double Star For Dictionary
--
def all_(**Any):
    print(Any["Name"])
all_(Name = "Manoj", age = 77)
-------------------------------------------------------------------------------
**)Global Variable
--->this global variable can be used for thourgh out the func.
Example :-
num = 9
def func():
    print(num)
func()
-------------------------------
**)Local Variable:-
--> This is used inside the functions..
ExamplE:-
def func():
    num = 9
    print(num)
func()
-----------------------------------
NOTE:-
--------
-->TO CHANGE THE GLOBAL VARIABLE BY USING KEYWORD (global) THAT CAN CHANGE COMPLETLY INSIDE AND OUTSIDE OF THE FUNCTIONS...
Example:-
Without using Global
num = 9
def func():
    num = 33
    print(num)
func()
print(num)
'''


num = 9
def func():
    global num
    num = 31
    print(num)
func()
print(num)














































