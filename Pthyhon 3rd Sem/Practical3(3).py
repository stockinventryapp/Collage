# Practical 3.3 : Write a Python program to display all prime numbers between two given numbers.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

i = 2
while num1 <= num2:
    i = 2

    while i <= num1 / 2:
        if num1 % i == 0:
            break
        i += 1

    if i > num1 / 2 and num1 > 1:
        print(num1)

    num1 += 1
