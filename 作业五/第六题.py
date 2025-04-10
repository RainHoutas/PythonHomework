# Example: Using list comprehension to create calories_list
foods = ["Apple", "Banana", "Orange", "Strawberry"]
calories = [52, 89, 47, 33]

# Create a list of tuples (food, calorie) using list comprehension
calories_list = [(food, calorie) for food, calorie in zip(foods, calories)]

# Output the result
print("Calories list:", calories_list)