# Practical 4.4 : Write a Python program to define a function that calculates compound interest using parameters and return values.

def factorial(n) :
    if n < 0 :
        print("Enter a non-negative number!!")
    elif n == 0 :
        return 1
    else :
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("The factorial is:", factorial(num))