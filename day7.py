#------------------------------------------------------Input Formatting from User------------------------------------------------------------------------------

'''
input()
-------------
The input() function is used to take input from the user.

1)int
---------

Example

num = int(input("Enter a number: "))
num2 = int(input("Enter a number:"))
print(num + num2)


2).String
-------------

Example:

how = input("Enter a char: ")
print(how + 'Sai')


3) float
------------------

Example:

num = float(input("Enter your salary: "))
print(num," is the monthly salary")


4)list
------------
Example:
group_ = list(map(int,input().split()))
print(group_)

example-2

group_ = list(input().split())
print(group_)

5)Tuple
-------------
Example

some = tuple(map(int,input().split()))
print(some)

group_ = tuple(input().split())
print(group_)

6)eval
--------------
Example:-
num_ = eval((input("Enter:")))
print(num,type(num_))

**) F string
name = input("Enter your name ")
age = int(input("Enter your age:"))
print(f"{name} your age is {age}")


***) name = input("Enter your name ")
age = int(input("Enter your age:"))
print(name,"Your is a cool",age)

**** Using modulus format
name = input("Enter your name ")
age = int(input("Enter your age:"))
print("My name is %s and i'm %d years old" %(name,age))


'''



































