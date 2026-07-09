#Lambda Function
'''
--->This is also called as annonymous function...
-->A lambda function can take n number of agruments but having only one expression

syntax --> lambda agruments : exxpression

**Single agruments and single expression 

some = lambda an : an + 5
print(some(10))


**Multipile agruments with single expression
some = lambda an,so : an * so
print(some(10,23))

**filter()
-------------
-->The filter() function is a built-in-function used to filter elements from an itterables such as list, tuple and set based on condition

syntax---> filter(function, itterable)

---> this filter() function returns filter object so we can convert thta into list, set and tuples......
------------------------------------------------------------------------------------------------------------------------------------------
#Even Number to print using Filter()
nums = [1,2,3,4,5,6]
rev = filter(lambda a : a%2==0,nums)
print(tuple(rev))
-------------------------------------------------------------
#Odd Number to print using Filter()
nums = [1,2,3,4,5,6]
rev = filter(lambda a : a%2 !=0,nums)
print(tuple(rev))
------------------------------------------------------------------

*List Comprehension
--------------------
--->This offers a shorter syntax when we want to create a new list from the old..

syntax--> variable_name = [expression loop condition]

With loop condition 
old = [1,2,3,4,5,7]
new_ = [i for i in old if i % 2 == 0]
print(new_)

without condition
old = [1,2,3,4,5,7]
new_ = [i for i in old]
print(new_)


#Dictionary Comprehension
------------------------------
--->This offers a shorter syntax when we want to create a new dict from the old dict

Syntax --> variable_name = [expression loop ]

old_dict = {1:2, 3:7, 5:6}
new_dict = {i:j for (i,j) in old_dict.items() if j % 2 == 0}
print(new_dict)

'''













































