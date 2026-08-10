# Practical 4.1 : Write a Python program to define a function that checks whether a number is a palindrome.

def pal(n) :
    temp = n
    rev = 0
    if n > 0 :
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if temp == rev :
        return True 
    else :
        return False

num = int(input("Enter a number: "))
if pal(num) :
    print(num,"is a palindrome number.")
else :
    print(num, "is not a palindrome number.")