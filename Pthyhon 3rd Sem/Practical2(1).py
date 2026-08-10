# Practical 2.1 : Write a Python program to check whether the entered number is positive, negative or zero.

num = float(input("Enter the number : "))

if num > 0 : 
    print ("The entered number ",num,"is positive")
elif num < 0 : 
    print ("The entered number ",num,"is negative.")
else : 
    print ("The entered number ",num,"is Zero. ")