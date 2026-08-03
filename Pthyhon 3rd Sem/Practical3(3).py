# Practical 3.3 : Write a Python program to display all prime numbers between two given numbers.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

for num in range(num1, num2 + 1) :
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)