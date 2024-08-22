# 1. with a program in Python to accept two number from theuser and calculate their square.

num1=float(input("Enter The value"))
num2=float(input("Enter the value"))

square1=num1*num1
print("Square of num1 is :",square1)

square2=num2*num2
print("Square of num2 is :",square2)

# 2. create a program to check if a number is even or odd.
# where a program in Python to accept a number from the user and using ternary operator check whether the number is even or odd.

num=int(input("Enter any number to test whether it is odd or even:"))

if (num % 2 )==0:
    print("The number is even")

else:
    print("The provided number is odd")