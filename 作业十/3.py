class Fridge:
    def __init__(self, name):
        self.name = name
        self.is_open = False
        self.contains = None

    def open_door(self, operator_name):
        if not self.is_open:
            print(f"{operator_name} 打开了 {self.name} 的门。")
            self.is_open = True
        else:
            print(f"{self.name} 的门已经是开着的。")

    def close_door(self, operator_name):
        if self.is_open:
            print(f"{operator_name} 关闭了 {self.name} 的门。")
            self.is_open = False
        else:
            print(f"{self.name} 的门已经是关着的。")

    def store_item(self, item_name):
        if self.is_open:
            if self.contains is None:
                self.contains = item_name
                print(f"{item_name} 进入了 {self.name}。")
            else:
                print(f"{self.name} 里面已经有 {self.contains} 了。")
        else:
            print(f"请先打开 {self.name} 的门才能放入东西。")

    def remove_item(self, item_name):
        if self.is_open:
            if self.contains == item_name:
                print(f"{item_name} 从 {self.name}出来了。")
                self.contains = None
            else:
                print(f"{self.name} 里面没有 {item_name}。")
        else:
            print(f"请先打开 {self.name} 的门才能取出东西。")


class Elephant:
    def __init__(self, name):
        self.name = name

    def open_fridge(self, fridge_instance):
        print(f"{self.name} 准备打开冰箱...")
        fridge_instance.open_door(self.name)

    def enter_fridge(self, fridge_instance):
        print(f"{self.name} 准备进入冰箱...")
        if fridge_instance.is_open:
            fridge_instance.store_item(self.name)
        else:
            print(f"冰箱门没开，{self.name} 进不去。")


    def close_fridge(self, fridge_instance):
        print(f"{self.name} 准备关闭冰箱...")
        fridge_instance.close_door(self.name)


# 创建对象
my_fridge = Fridge("海尔冰箱")
daxiang = Elephant("大象Coco")

# 模拟大象进冰箱的过程
print("---开始模拟大象进冰箱---")
daxiang.open_fridge(my_fridge)
daxiang.enter_fridge(my_fridge)
daxiang.close_fridge(my_fridge)

print("\n---冰箱当前状态---")
print(f"冰箱名称: {my_fridge.name}")
print(f"冰箱门是否打开: {'是' if my_fridge.is_open else '否'}")
print(f"冰箱里有什么: {my_fridge.contains if my_fridge.contains else '空的'}")

print("\n---尝试再次操作---")
daxiang.open_fridge(my_fridge) # 尝试打开已关闭的冰箱
my_fridge.remove_item(daxiang.name) # 大象出来
daxiang.close_fridge(my_fridge) # 关闭冰箱