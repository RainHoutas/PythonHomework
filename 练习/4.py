class Circle:
    banjing = 0
    color = "red"
    def __init__(self, banjing, color):
        self.banjing = banjing
        self.color = color
    def mianji(self):
        return 3.14 * self.banjing ** 2
    def changdu(self):
        return 2 * 3.14 * self.banjing

yuan = Circle(5, "blue")
print(f"圆的半径为：{yuan.banjing}")
print(f"圆的颜色为：{yuan.color}")

#先定义一个类，里面有两个属性和两个方法，方法可以计算圆的面积和周长
