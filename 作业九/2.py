class House:
    total_houses = 0  # 类属性，用于计算房子的总数

    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        House.total_houses += 1  # 每创建一个实例，总数加1

    def calculate_area(self):
        """计算房子的面积"""
        return self.length * self.width

# 创建House类的多个实例对象
house1 = House("温馨小屋", 10, 8)
house2 = House("豪华别墅", 20, 15)
house3 = House("乡村小院", 12, 10)

# 打印房子的总数
print(f"房子的总数: {House.total_houses}")

# 打印每个房子的信息和面积
print(f"\n房子1: {house1.name}, 长: {house1.length}, 宽: {house1.width}, 面积: {house1.calculate_area()}")
print(f"房子2: {house2.name}, 长: {house2.length}, 宽: {house2.width}, 面积: {house2.calculate_area()}")
print(f"房子3: {house3.name}, 长: {house3.length}, 宽: {house3.width}, 面积: {house3.calculate_area()}")