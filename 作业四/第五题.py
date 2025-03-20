def solve_chicken_rabbit(h, f):
    for chickens in range(h + 1):
        rabbits = h - chickens
        if chickens * 2 + rabbits * 4 == f:
            return chickens, rabbits
    return None, None

h = int(input("Enter the total number of chickens and rabbits: "))
f = int(input("Enter the total number of legs: "))
chickens, rabbits = solve_chicken_rabbit(h, f)
if chickens is not None:
    print(f"Chickens: {chickens}, Rabbits: {rabbits}")
else:
    print("No solution")