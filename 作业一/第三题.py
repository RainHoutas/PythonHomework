import math

def calculate_circle_area_and_diameter(radius):
    area = math.pi * (radius ** 2)
    diameter = 2 * radius
    return area, diameter

radius = float(input("请输入圆的半径: "))
area, diameter = calculate_circle_area_and_diameter(radius)
print(f"圆的直径为: {diameter}")
print(f"圆的面积为: {area}")