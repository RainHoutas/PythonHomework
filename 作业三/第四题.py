s = '000Luoyang Normal University, Luoyang City, Henan Province000'

# (1) Find the index of 'Luoyang'
index = s.find('Luoyang')
print(f"Index of 'Luoyang': {index}")

# (2) Count occurrences of 'Luoyang'
count = s.count('Luoyang')
print(f"Occurrences of 'Luoyang': {count}")

# (3) Replace '000' with space
s_replaced = s.replace('000', ' ')
print(f"Replaced string: {s_replaced}")

# (4) Convert all letters to uppercase
s_upper = s_replaced.upper()
print(f"Uppercase string: {s_upper}")

# (5) Remove leading and trailing spaces
s_trimmed = s_upper.strip()
print(f"Trimmed string: {s_trimmed}")

# (6) Split the string by spaces
s_split = s_trimmed.split()
print(f"Splitted string: {s_split}")