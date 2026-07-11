'''
----------Generators------------
-->This generators is special function that returns the itertor.instead of returning all the values at once.......
--> Here we are going to use yield keyword


def some():
    yield 1
    yield 2
    yield 3
so = some()
print(next(so))
print(next(so))

Working of Generator
-----------------------
-->When a function is called
-->It does NOT EXCUTES THE FUNCTION immediately........
-->It will returns the generator object
--->Then then function will pasues at each yield...
--->When the Next() is called again, execution resumes from where it stoped..

#1.Example:-

def demo():
    print("Start")
    yield 1

    print("Middle")
    yield 2

    print("End")
    yield 3

how = demo()
print(next(how))
print(next(how))

#2.Example:-

def how(so):
    for i in range(so):
        yield i * i
any_ = how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))


#3.Example:- Without Generators 
def sqn(n):
    for j in range(n):
        print(j * j)
sqn(5)



#next() Keyword
-----------------
-->the next() function is used to retrive the next value from a generator
Example:-

def how(so):
    for i in range(so):
        yield i * i
any_ = how(5)
print(next(any_))
print(next(any_))


#StopIteration
-----------------
-->Calling next() function after all values retrieve then it will raise StopIteration exception
Example:-

def how(so):
    for i in range(so):
        yield i * i
any_ = how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))

Generators Expression
----------------------
--> The generator expression is similar to a list comprehension but uses parenthesis () instead of []

'''

gen = (x * x for x in range(5))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
















