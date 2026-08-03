# Practical 4.4 : Write a Python program to define a function that calculates compound interest using parameters and return values.

def factorial(n) :
    answer = 1
    while n > 0 :
        answer *= n
        n -= 1
    print("The factorial is", answer)

num = int(input("Enter a number: "))
factorial(num)
