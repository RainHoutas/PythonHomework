# Original list
s = [9, 7, 8, 3, 2, 1, 5, 6]

# Transform the list
s = [x**2 if x % 2 == 0 else x for x in s]

# Output the result
print("Transformed list:", s)