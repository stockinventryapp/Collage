# ============================================================
#                       PYTHON PROGRAMS 
# ============================================================


# ============================================================
# PRACTICAL 1.1
# Write a Python program to accept two numbers from the user
# and perform addition, subtraction, multiplication, and division.
# ============================================================

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)


# ============================================================
# PRACTICAL 1.2
# Write a Python program to calculate the area and circumference
# of a circle by accepting the radius from the user.
# ============================================================

radius = float(input("Enter the radius of the circle: "))

area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius

print("Area of the circle:", area)
print("Circumference of the circle:", circumference)


# ============================================================
# PRACTICAL 1.3
# Write a Python program to convert temperature from Celsius
# to Fahrenheit and Fahrenheit to Celsius based on user choice.
# ============================================================

choice = int(input("Enter 1 for Celsius to Fahrenheit or 2 for Fahrenheit to Celsius: "))
temperature = float(input("Enter the temperature: "))

if choice == 1:
    fahrenheit = (temperature * 9 / 5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)
elif choice == 2:
    celsius = (temperature - 32) * 5 / 9
    print("Temperature in Celsius:", celsius)
else:
    print("Invalid choice.")


# ============================================================
# PRACTICAL 2.1
# Write a Python program to check whether the entered number
# is positive, negative or zero.
# ============================================================

num = float(input("Enter the number : "))

if num > 0:
    print("The entered number", num, "is positive")
elif num < 0:
    print("The entered number", num, "is negative.")
else:
    print("The entered number", num, "is Zero.")


# ============================================================
# PRACTICAL 2.2
# Write a Python program to find the largest of three numbers
# entered by the user using nested if-else statements.
# ============================================================

num1 = float(input("Enter the First Number :  "))
num2 = float(input("Enter the Second Number :  "))
num3 = float(input("Enter the Third Number :  "))

if num1 > num2:
    if num1 > num3:
        print(num1, "is largest number.")
    else:
        print(num3, "is largest number.")
else:
    if num2 > num3:
        print(num2, "is largest number.")
    else:
        print(num3, "is largest number.")


# ============================================================
# PRACTICAL 2.3
# Write a Python program to calculate the grade of a student
# based on marks entered by the user.
# ============================================================

marks = int(input("Enter your marks : "))

if marks > 100 or marks < 0:
    print("Enter the valid marks between (0-100)!!")
elif marks <= 100 and marks > 90:
    print("Your Grade is : A+")
elif marks <= 90 and marks > 80:
    print("Your Grade is : A")
elif marks <= 80 and marks > 70:
    print("Your Grade is : B+")
elif marks <= 70 and marks > 60:
    print("Your Grade is : B")
elif marks <= 60 and marks > 50:
    print("Your Grade is : C+")
elif marks <= 50 and marks > 40:
    print("Your Grade is : C")
else:
    print("You have a backlog.")


# ============================================================
# PRACTICAL 3.1
# Write a Python program to generate the Fibonacci series
# up to n terms entered by the user.
# ============================================================

c = int(input("Enter the number of terms : "))
a = 0
b = 1
counter = 0

print("Fibonacci sequence:")

while counter < c:
    print(a, end=' ')
    nth = a + b

    # Update values
    a = b
    b = nth
    counter += 1


# ============================================================
# PRACTICAL 3.2
# Write a Python program to find the factorial of a given
# number using a while loop.
# ============================================================

num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
else:
    while num > 0:
        factorial *= num
        num -= 1

    print("The factorial is", factorial)


# ============================================================
# PRACTICAL 3.3
# Write a Python program to display all prime numbers
# between two given numbers.
# ============================================================

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

for num in range(num1, num2 + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


# ============================================================
# PRACTICAL 4.2
# Write a Python program to define a function that calculates
# simple interest using parameters and return values.
# ============================================================

def simple_interest(p, r, t):
    return (p * r * t) / 100


p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time period: "))

si = simple_interest(p, r, t)

print("The simple interest is:", si)


# ============================================================
# PRACTICAL 4.4
# Write a Python program to define a function that calculates
# compound interest using parameters and return values.
# ============================================================

def factorial(n):
    if n < 0:
        print("Enter a non-negative number!!")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter a number: "))

print("The factorial is:", factorial(num))