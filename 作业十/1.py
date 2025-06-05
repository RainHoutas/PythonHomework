import math

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def calculate_perimeter(self):
        """计算圆的周长"""
        return 2 * math.pi * self.radius

    def calculate_area(self):
        """计算圆的面积"""
        return math.pi * (self.radius ** 2)

# 创建Circle类的实例对象
my_circle = Circle(5, "红色")

# 计算并打印周长和面积
perimeter = my_circle.calculate_perimeter()
area = my_circle.calculate_area()

print(f"圆的半径: {my_circle.radius}")
print(f"圆的颜色: {my_circle.color}")
print(f"圆的周长: {perimeter:.2f}")
print(f"圆的面积: {area:.2f}")