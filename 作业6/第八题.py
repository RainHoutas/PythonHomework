import random


A = {random.randint(0, 10) for _ in range(10)}
B = {random.randint(0, 10) for _ in range(10)}


print("Set A:", A)
print("Set B:", B)
print("Length of A:", len(A))
print("Length of B:", len(B))
print("Max of A:", max(A))
print("Max of B:", max(B))
print("Min of A:", min(A))
print("Min of B:", min(B))

print("Union of A and B:", A | B)
print("Intersection of A and B:", A & B)
print("Difference of A and B (A - B):", A - B)