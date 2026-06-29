#================================================================================================================================================================
#-----------------------------------------------------------------------List DataTypes---------------------------------------------------------------------------
#---> List is a collection of different datatypes thta are enclosed in [].
#--->list is muttable.
#======================================
#Methods
#======================================
#--------------------------------------------------------------------------------------------------------------
#1) append()
#--> Adds the new item to the List, But it will adds in the last index position.
#-->
#Example:
'''
any_ = [1,2,3,4]
print(any_)
any_.append(5)
print(any_)
any_.append(12)
print(any_)
any_.append('python')
print(any_)
'''
#-------------------------------------------------------------------------------------------------------------------
#muttabl                                           immutable
#=========                                        ============
#*the datatype can be modified                    *Can't be modified
#List                                             String
'''
any_ = [1,2,3,4]                                  so ='Python is a Language
print(any_)                                       print(so.replace('Python','Java'))
any_.append(5)                                    print(so)
print(any_)
any_.append(12)
print(any_)
'''
#----------------------------------------------------------------------------------------------------------------------
#2)Extend()
#--->This is also add a item in the last index position, but it will give each value in the each index position.
#-->it will take
#Example:
"""
any_ = [1,2,3,4,5]
any_.extend('python')
print(any_)
print(len(any_))
"""
#---------------------------------------------------------------------------------
#Indexing in List**
'''
any_ = [1,2,'Python is a language',[45,78,"Java is a language",[1,23],90],'Hello']
print(any_[3][3][1])'''
#---------------------------------------------------------------------------------------
#3)Pop()
#-->Pop is used to delete the value from the list, but it will delete based on index position
#Syntax---> variable_name.pop(index_position)
#Example:

any_ = [1,2,45,78,23,90]
any_.pop(4)
print(any_) 
#--------------------------------------------------------------------------------------------
#4)remove()
#-->remove is used to delete the item from the list, but it will delete based on the Value
#Syntax-->Variable_name.remove(value)
#Example:

any_ = [1,2,45,78,23,90]
any_.remove(45)
print(any_) 
#----------------------------------------------------------------------------------------------------
#=====================================================================================================
#Tuple
#--->Tuple is a collection of different datatypes represent in () and seperated by
#--> this is immutable
#================================================================================================
#Methods in tuple
#1)index()
'''
how = (1,2,3,4,5,"Python",[4,5],(27,31))
print(how.index('Python')) '''
#-----------------------------------------------------------
#2)count()
'''
how = (1,2,3,4,5,"Python",[4,5],(27,31))
print(how.count('Python')) '''
#============================================================
#*Sort--> it will sort 
#Sorted
"""
any_ = [27,11,18,31]
print(sorted(any_))
print(any_)
any_.sort()
print(any_)
"""
