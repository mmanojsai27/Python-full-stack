#Passing By value
'''
def some(a):
    for j in a:
        print(j)
some([1,2,3])
'''

#Passing By reference
'''
a = (1,2,3,4)
def some(a):
    for j in a:
        print(j)
some(a)

#return Keyword
------------------
---> In a function if a return is executed then it will exit from the function with certain returned values..


def myfunc(b):
    return 5 + b
a = myfunc(10)
c = myfunc(100)
print(a)
print(c)


import builtins

builtin_functions = [name for name in dir(builtins)

                     if callable(getattr(builtins,name))]
print(builtin_functions)
print(f"Total-built-in functions are (len(builtin_functions))")
'''

#Recursive Function
'''
--->Recursive function that calls itself repeatedly until a specified condition is met...

syntax
------
def func_name(parameter):
    if condition: -->Base case
        return statement
    else:
        return statement
print(func_name(arguments))
'''

'''
def func_name(num):
    if num == 1:
        return 1
    else:
        return num * func_name(num-1)
num = 10
print(func_name(num))
'''















































