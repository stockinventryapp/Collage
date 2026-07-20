# Practical 2.3 : Write a Python program to calculate the grade of a student based on marks entered by
# the user.

marks = int(input("Enter your marks : "))

if marks > 100 or marks < 0 :
    print ("Enter the valid marks between (0-100)!!")
elif marks <= 100 and marks > 90 :
    print ("Your Grade is : A+")
elif marks <= 90 and marks > 80 :
    print ("Your Grade is : A")
elif marks <= 80 and marks > 70 :
    print ("Your Grade is : B+")
elif marks <= 70 and marks > 60 :
    print ("Your Grade is : B")
elif marks <= 60 and marks > 50 :
    print ("Your Grade is : C+")
elif marks <= 50 and marks > 40 :
    print ("Your Grade is : C")
else :
    print ("You have a backlog.")