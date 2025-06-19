def fibonacci(n):
    list_result = [0,1]
    a,b = 0,1
    while len(list_result) < n:
        a, b = b ,a+b
        list_result.append(b)
    return list_result

print(fibonacci(100))