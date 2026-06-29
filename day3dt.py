#============================================================#DataTypes====================================================================================

int
#----

num = 8


#----------
float
#----------------
'''
num_2 = 7.89
'''
'''
num_2 = 7.89
num = 6.89
print(num // 2)
'''

##string
#---------------
#---> String is a squence of char that are enclosed in , ' ', " ", ''' '''
#---> String is immutale

#concatination
#----------------------
#--> Here, the (+) operator act as a concatinate more than 2 string..
'''
so = "python"
any_ = " is a language"
print(so + any_)
'''
#=========================================================================================================
#indexing
#--->This is used to access the particular char in the string by passs index position value.
#----> Idex start from 0........
#--->We have negativw idexing to count position from last to first..
'''
so = "Python is a Language"
print(so[12])

so = "Python is a Language"
print(so[-2])
'''

#=======================================================================
#Methods
#=====================================================================

#1)replace()
#--->This method is used to change any substring inn that particular string.
##--->Syntax
#------> variable_name.replace("old_string",new_string,count)
#Example
'''
so = "Python is a Language"
print(so.replace("Python","java"))
'''
#-------------------------------------------------------------------------------------
#2)join()
#--->This method used to add new substring after each char in the string.
#synatx--->
''' "string".join(variable_name) '''
'''
so = "Python is a Language"
print(" ".join(so))
'''
#----------------------------------------------------------------------------------
#3)split()
#---->This method can divide the string into different index into list, based on the string pass by us...
#Syntax--->variable_name.split('substring')

so = "Python is a Language"
print(so.split(" is "))

#------------------------------------------------------------------------------
#4)count()
#--->This method is used to count string substring in the particular string and also specify the index position
#Syntax ----> variable _name.count("substring",start index,ending index)
'''
so = "Python is a Language"
print(so.count("a",0,12))
'''
#==========================================================================================================================
#string Bulit-in Functions
#========================================================================================================

#-------------------------------
#1)len()
#--->This will find the length of the string, which is number char present in that string..
'''
so = "Python is a Language"
print(len(so))
'''
#--------------------------------------------
#2)max()
#---->will the max char in the string
'''
so = "Python is a Language"
print(max(so))
'''
#-------------------------------------------
#3)min()
#will the min char in the string
'''
so = "Python is a Language"
print(min(so))
'''
#=====================================================================================================================
