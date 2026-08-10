# Practical 4.4 : Write a Python program to compute the factorial of a given number using a recursive function.

def factorial(n) :
    if n < 0 :
        print("Enter a non-negative number!!")
    elif n == 1 :
        return 1
    else :
        return n * factorial(n - 1) # till the factorial of 1 is called the earlier answers stored in stack

num = int(input("Enter a number: "))
print("The factorial is:", factorial(num))