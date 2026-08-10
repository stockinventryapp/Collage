# Practical 4.3 : Write a Python program to define a function that returns the maximum and minimum values from a list.
def max_min(n):
   return max(n), min(n)

# Or you can implement it manually without using built-in functions:
#def max_min(n):
#    maximum = n[0]
#    minimum = n[0]
#
#    for i in n:
#        if i > maximum:
#            maximum = i
#        if i < minimum:
#            minimum = i

#    return maximum, minimum


n = [2, 5, 1, 8, 3]
maximum, minimum = max_min(n)
print("Maximum value:", maximum)
print("Minimum value:", minimum)