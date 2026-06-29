#===================================================================
#Dictionary
#-->Dict is a key : value pair seperated by :, and keys are unique.
#-->in the place of keys we have use immutable data types...
'''
details_ = {"name" : "Manoj",
            1: "number",
            (6,7): [1,2]}
print(details_)
'''
#========================================================================
#methods
#===================================================
#1)Keys()
#--->Used to get all the keys from the dict.
#Syntax--> Variable_name.keys().
#Example:-
"""
details_ = {"Name" : "Manoj",
            "Age" : 31,
            "Gender" :"Male"}
print(details_.keys()) """
#======================================================
#2)values()
#--->Used to get all the values frim the dict
#Synatx-->variable.name.values().
"""
details_ = {"Name" : "Manoj",
            "Age" : 31,
            "Gender" :"Male"}
print(details_.values()) """
#=======================================================
#3)items()
#--->Used to get both key and values from in a pair
#synatax-->variable_name.items()
'''
details_ = {"Name" : "Manoj",
            "Age" : 31,
            "Gender" :"Male"}
print(details_.items())
'''
#=================================================
'''
any_ = [23,311,27,7,11]
print(any_[0])
details_ = {"Name" : "Manoj",
            "Name_1" : "Arun",
            "Age": 31,
            "Age_1": 26,
            "Gender" :"Male",
            "Gender_1" : "Male"}
print(details_['Name_1'])'''
#=================================================
#4)Clear()
#---------------------
"""
details_ = {"Name" : "Manoj",
            "Age" : 31,
            "Gender" :"Male"}
details_.clear()
print(details_)
"""
#======================================
#5)Update()
"""
details_ = {"Name" : "Manoj",
            "Age" : 31,
            "Gender" :"Male"}
details_.update({"Name":"Mortha"})
details_.update({"Age":"27"})
print(details_)
"""
#=====================================
#**************SET'S************
#====================================
#--->set is collection unordered elements that are seperated by ,
#--->set is muttable
#--->can remove duplicate value by itself....
'''
go = {1,2,3,4,5,2}
print(go)
'''
#---------------------------------------------------------------
#Methods
#----------------
#1)Union()-(|)
#--->Combine the Elements from both set
#Synatx---> set_1.union(set_2)
#Example
"""
go = {1,2,3,4,5,2}
so = {11,22,33,7,}
print(go | so)
print(so.union(go)) """
#-------------------------------------------------------
#2)Intersections()(&)
#--->Common Elements from the both sets
#Synatx--> Set_1.intersection(Set_2)
'''
go = {1,2,3,4,5,2}
so = {11,22,33,5,2}
print(go & so)
print(go.intersection(so))'''
#==============================================================
#3)Symmetric Difference()(^)
#--->all different elements from both sets
#Synatx-->Set_1.symmetric_difference(Set_2)
''''
go = {1,2,3,4,5,2}
so = {11,22,33,5,2}
print(go ^ so)
'''

#4).add()
"""
--->Used to add new Elements into Set

go = {1,2,3,4,5,2}
go.add(7)
print(go)"""

#5).remove()
"""
--->To del the elements from set
eg:=
go = {1,2,3,4,5,2}
go.remove(3)
print(go)
"""

#6)Discard()

#--->Discard will del the value 
go = {1,2,3,4,5,2}
go.remove(7)
print(go)





















































































