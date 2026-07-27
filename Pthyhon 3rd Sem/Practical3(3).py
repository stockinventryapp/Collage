# Practical 3.3 : Write a Python program to display all prime numbers between two given numbers.

num = int(input("Enter the number: "))

i = 2

while i <= num/2:
    if num % i == 0:
        print(num, "is not a prime number")
        break
    i += 1
else : 
    print(num, "is a prime number")
