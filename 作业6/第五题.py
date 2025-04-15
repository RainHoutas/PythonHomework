import random


n = int(input("Enter the number of random integers (N <= 1000): "))


random_numbers = [random.randint(1, 1000) for _ in range(n)]


unique_sorted_numbers = sorted(set(random_numbers))


print("\nSorted unique student IDs:")
print(unique_sorted_numbers)