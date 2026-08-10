# Practical 4.3 : Write a Python program to define a function that returns the maximum and minimum values from a list.
def max_min(n):
    return max(n), min(n)

n = [3, 10, 6, 18, 12]
maximum, minimum = max_min(n)
print("Maximum value:", maximum)
print("Minimum value:", minimum)