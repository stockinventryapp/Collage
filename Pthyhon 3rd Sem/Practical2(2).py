# Practical 2.2 : Write a Python program to find the largest of three numbers entered by the user using
# nested if–else statements.

num1 = float(input("Enter the First Number :  "))
num2 = float(input("Enter the Second Number :  "))
num3 = float(input("Enter the Third Number :  "))

if num1 > num2 :
    if num1 > num3 :
        print(num1, " is largest number.")
    else :
        print(num3, " is largest number.")

else :    
    if num2 > num3 :
        print(num2, " is largest number.")
    else :
        print(num3, " is largest number.")