num_list = [23, 11, 12, 23, 9, 2, 1, 4]

def has_duplicates(lst):
    return len(lst) != len(set(lst))

if has_duplicates(num_list):
    print("The list contains duplicate elements.")
else:
    print("The list does not contain duplicate elements.")