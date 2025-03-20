def series_sum(n):
    if n >= 10:
        return "data error!"
    total = 0
    current_number = 0
    for i in range(1, n + 1):
        current_number = current_number * 10 + i
        total += current_number
    return total

n = int(input("Enter a number less than 10: "))
result = series_sum(n)
print(result)