class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("动物在叫")

class Dog(Animal):
    def speak(self):
        print(f"{self.name}狗叫")

class Cat(Animal):
    def speak(self):
        print(f"{self.name}猫爹哈哈气")

dog = Dog("王八")
cat = Cat("金鱼")
dog.speak()
cat.speak()