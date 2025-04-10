# Create a list of your favorite foods
my_favorite_foods = ["Pizza", "Sushi", "Burger", "Pasta"]

# Copy the list to create a friend's favorite foods list
friends_favorite_foods = my_favorite_foods[:]

# Modify the friend's favorite foods list
friends_favorite_foods.append("Ice Cream")  # Add a new food
friends_favorite_foods[1] = "Tacos"        # Modify an existing food
friends_favorite_foods.remove("Burger")    # Remove a food

# Print both lists
print("My favorite foods:", my_favorite_foods)
print("Friend's favorite foods:", friends_favorite_foods)