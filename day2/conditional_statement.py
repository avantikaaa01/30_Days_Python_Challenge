# Input a number and check if it is even or odd
a = int(input("Enter a number"))
if a % 2 ==0:
    print("It is even number")
else:
    print("It is odd number")


# Hardcoded username/password check
username = input("enter username")
password = int(input("enter password"))
if(username == "admin" and password == 1234):
    print("login Successfull")
else:
    print("Invalid username and password")

# Input 3 numbers and print the largest
num1 = int(input("enter the num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))

if(num1> num2 and num1 > num3):
    print(num1, " is a greater")
elif(num2> num1 and num2 > num3):
    print(num2, " is a greater")
else:
    print(num3, " is greater")

