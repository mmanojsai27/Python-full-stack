#---------------Error Handling-----------------#
'''
Syntax Error
-------------
for j in range(1,10:
    print(j)

o/p -- SyntaxError
-------------------
for j in range(1,10):
    print(j)

Indentation Error
------------------

    a = 20
for j in range(a):
    print(j)
else:
print()

O/p:---IndentationError

Value error
----------

num = int(input("Enter a num: "))

O/P :- ValueError
----------------------------------
 Try
-----

The try block will test the code for error

Syntax -- try:

 except
---------
This except let us handle the error in the code

Syntax -- except:

else:
finally:
--------------------------------------

try:
    num = int(input("Enter a num: "))
except ValueError:
    print('Will get name error')
----------------------------------------
'''

try:
    num = int(input("Enter a num: "))
    num_2= int(input("Enter a num: "))
    print(num/num_2)
except ZeroDivisionError:
    print('Will get zerodivision error')
except ValueError:
    print('Will get value error')
else:
    print('no error')
finally:
    print("end")
