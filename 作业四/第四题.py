def count_characters(s):
    letters = spaces = digits = others = 0
    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isspace():
            spaces += 1
        elif char.isdigit():
            digits += 1
        else:
            others += 1
    return letters, spaces, digits, others

s = input("Enter a string: ")
letters, spaces, digits, others = count_characters(s)
print(f"Letters: {letters}, Spaces: {spaces}, Digits: {digits}, Others: {others}")