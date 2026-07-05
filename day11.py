#Palindrom Program.
'''
so = input("Enter a Word: ")
empty = " "
for j in so:
    empty = j + empty
if empty == so:
    print(f"{so} It is Palindrom.")
else:
    print(f"{so} It is Not a Palindrom.")
'''

#Fibonacci Sequence
'''
num = 0
num2 = 1
limit = int(input("Enter A Number: "))
print(num,num2, end = " ")
for i in range(1,limit + 1):
    all_ = num + num2
    num = num2
    num2 = all_
    print(all_,end = " ")
'''

#Calculator
'''
Val_1 = int(input("Enter A Number: "))
Val_2 = int(input("Enter A Number: "))

user_in = int(input("Enter \n1.Add \n2.Subb \n3.Mult \n4.Pow \n5.Div \n6.SQ Root: "))
if user_in == 1:
    print(Val_1 + Val_2)
elif user_in == 2:
    print(Val_1 - Val_2)
elif user_in == 3:
    print(Val_1 * Val_2)

elif user_in == 4:
    print(Val_1 ** Val_2)
elif user_in == 5:
    print(Val_1 / Val_2)
else:
    print(Val_1 ^ Val_2)
'''

#Table's
'''
Table_ = int(input("Enter A Number: "))
for val in range(1,13):
    print(f"{Table_} X {val} = {Table_ * val}")
'''

#Perfect Number:
'''
num = int(input("Enter A Number: "))
sum_ = 0
for j in range(1,num):
    if num % j == 0:
        sum_ += j
if sum_ == num:
    print(f"{num} Is A Perfect Number.")
else:
    print(f"{num} Is Not A Perfect Number.")
'''
#ATM Transcations Process

details_ = {"Name" : "Manoj",
            "ATM PIN":"3127",
            "Balance":50000}
print("-----------WELCOME To ATM---------------------")
pin = input("Enter Your PIN: ")
if len(pin) == 4:
    if pin == details_["ATM PIN"]:
        user_in = int(input("Enter \n1.Withdrawl \n2.Desposit \n3.Balance."))
        if user_in == 1:
            Withdrawl = int(input("Enter Your Amount: "))
            if Withdrawl <= details_["Balance"]:
                if Withdrawl % 100 == 0:
                    details_["Balance"] -= Withdrawl
                    print(f"Your Withdrawl Amount {Withdrawl} And Your Balance {details_["Balance"]}")
                else:
                    print("Entered Invalid Amount And Enter Again.")
            else:
                print(f"Your Balance {details_["Balance"]},\nEnter Less Amount: ")

        if user_in == 2:
            Desposit = int(input("Enter Your Desposit Amount Only In : 100's,200's,500's."))
            if Desposit % 100 == 0:
                details_["Balance"] += Desposit
                print(f"You Have Desposited {Desposit} And Your Total Savings Amount Was {details_["Balance"]}")
            else:
                print(f"Atm Can Not Accept The Change Please Desposit In 100's,200's,500's")

        if user_in == 3:
            print(f"Your Total Savings Amount Was {details_["Balance"]}")
    else:
        print("You Entered Invalid Pin")
else:
    print("Your Is Too lenght Enter Again")
    
            
        
            












    
