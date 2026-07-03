#2)loop Statements--------------
'''
1)for loop
-----------------
---> A for loop is used to itterate over a squence, list, tuple
example:-
any_ = "Python is language"
for j in any_:
    print(j)


num2 = [1,2,34,5,6,7,11]
for num3 in num2:
    print(num3)

*dict
any_ = {"Name":"Manoj",
        "Role":"Trainee"}
for key in any_.values():
    print(key)

--------------------------------------
Else in for loop
---------------------
--->The else block will excuted after the for loop,but incase the loop is breaked then it will never
entered in the else block.
*Without Break
any_ = [1,2,3,4,5,6]
for val in any_:
    print(val)
else:
    print("Program Ended")

any_ = [1,2,3,4,5,6]
for val in any_:
    print(val)
    if val == 4:
         break
else:
    print("Program Ended")
-------------------------------------------------------------
2)while loop
---> The while loop will excuted untill the condition become true.......
Example:
--
i = 1        
while i < 8: 
    print(i) 
-------------------
i = 1
while i < 8:
    print(i)
    i += 1'''
'''----------------------------------------------------------------------------'''
               #3)  Control Statements
               '''----------------------'''
'''----------------------------------------------------------------------'''
'''
1.break()
---------
-->The break is use to exit from the loop

Example:

any_ = [1,2,3,4,5,6]
for val in any_:
    print(val)
    if val == 4:
         break
else:
    print("Entered")
----------------------------------------------------------------------
2)continue()
--->The continue will skip the current itteration
any_ = [1,2,3,4,5,6]
for j in any_:

    if j == 3:
         continue
    print(j)    
else:
    print("Entered")
--------------------------------------------------------------------------
3)pass()
---> It is Space Holder
any_ = [1,2,3,4,5,6]
for j in any_:

    if j == 3:
         continue
    print(j)    
else:
    pass
----------------------------------------------------------------------------
** range()
--->range () is a in-bulit function that is used to genrate a squence upto a limit.

Synatx --> range(start,end, step)

Example:
all_ = [1,2,3,4,5]
for j in range(7,32):
    print(j)
-----------------------------------------------------------------------------------
**assert Keyword()
-----------------
---> It will used to check the condition,but it will raise an error icase it is Flase
Example:
age = int(input("Enter your age:  "))
assert age >= 18,"You Must Have 18 Years"

'''





























    

