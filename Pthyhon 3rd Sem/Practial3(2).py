# Practical 3.2 : Write a Python program to find the factorial of a given number using a while loop.

num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
else :
    while num > 0 :
        factorial *= num
        num -= 1
    print("The factorial is", factorial)
