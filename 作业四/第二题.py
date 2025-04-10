def triangle_type(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Equilateral triangle"
        elif a == b or b == c or a == c:
            return "Isosceles triangle"
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Right triangle"
        else:
            return "Scalene triangle"
    else:
        return "Not a triangle"

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
result = triangle_type(a, b, c)
print(result)
