#prime number
'''
num = int(input("Enter a Number: "))
count = 0
for j in range(1,num +1):
    if num % j == 0:
        count += 1
        #print(count)
if count == 2:
    print(f"{num} Is a Prime.")
else:
    print(f"{num} Is Not a Prime.")
'''
#To Print the prime numbers.
'''
limit_ = int(input("Enter a Number."))

for j in range(1, limit_+1):
    count = 0
    for i in range(1,j +1):
        if j % i == 0:
            count += 1
    if count == 2:
        print(f"{j} Is A Prime.")
'''
#To Print the '*' Right angle Triangle
'''
num = 7
for j in range(1,num + 1):
    for i in range (1,j + 1):
        print("*" , end = " ")
    print(" ")    
'''

#To Print the
'''
num = 7
for j in range(1,num+1):
    for i in range(1,j+1):
        print(j, end = " ")
    print(" ")
'''
#To print The
'''
num = 4
count = 0
for j in range(1,num + 1):
    for i in range(1,j +1):
        count +=1
        print(count, end=" ")
    print(" ")
'''

#To print the
'''
num = 5
count = 0
for j in range(num,0,-1):
    for i in range(1,j + 1):
        count += 1
        print(i,end=" ")
    print(" ")
'''
#Amstorng num
'''
am_str = int(input("Enter the Number: "))
lenght_ = len(str(am_str))
all_sum = 0
for j in str(am_str):
    all_sum += int(j) ** lenght_
if all_sum == am_str:
    print(f"{am_str} Is a Amstrong.")
else:
    print(f"{am_str} Is Not a Amstrong.")
'''

#Parmid
num = 7
for j in range(num):
    print(" " *(num -j -1),end = " ")
    print("*" *(2 * j + 1))


















