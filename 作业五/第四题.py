import random
import string

# Step 1: Define an empty list
chars_list = []

# Step 2: Randomly generate 6 characters (letters or digits) and add them to the list
for _ in range(6):
    chars_list.append(random.choice(string.ascii_letters + string.digits))

# Step 3: Join the list elements into a string and output the result
verification_code = ''.join(chars_list)
print("Generated verification code:", verification_code)