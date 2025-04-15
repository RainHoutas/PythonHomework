
favorite_dict = {}


n = int(input("Enter the number of categories: "))


for _ in range(n):
    category = input("Enter a category (e.g., food, pet, sport): ")
    items = input(f"Enter your favorite items for {category}, separated by commas: ").split(",")
    favorite_dict[category] = [item.strip() for item in items]  # Strip whitespace from each item

print("\nFavorite Dictionary:")
print(favorite_dict)