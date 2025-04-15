
str = 'skdaskerkjsalkj'


letter_counts = {}

for char in str:
    if char in letter_counts:
        letter_counts[char] += 1
    else:
        letter_counts[char] = 1


print("Letter counts:", letter_counts)