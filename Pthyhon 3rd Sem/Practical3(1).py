c = int(input("Enter the number of terms : "))
a = 0
b = 1
counter = 0

print("Fibonacci sequence:")
while counter < c :
    print(a , end=' ')
    nth = a + b
    # update values
    a = b
    b = nth
    counter += 1


