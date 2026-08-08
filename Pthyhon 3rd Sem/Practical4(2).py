# Practical 4.2 : Write a Python program to define a function that calculates simple interest using parameters and return values.

def simple_interest(p, r, t):
   
    return (p * r * t) / 100

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time period: "))

si = simple_interest(p, r, t)
print("The simple interest is:", si)