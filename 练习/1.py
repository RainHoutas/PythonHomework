def issanjiaoxing (first, second, third):
    if first + second > third and first + third > second and second + third > first:
        return True
    else:
        return False

def mianji (first, second, third):
    p = (first + second + third) / 2
    return (p * (p - first) * (p - second) * (p - third)) ** 0.5

def main ():
    first = int(input("第一条边"))
    second = int(input("第二条便："))
    third = int(input("第三条便"))
    if issanjiaoxing(first, second, third):
        print("可以构成三角形")
        print(f"三角形的面积为：{mianji(first, second, third)}")
    else:
        print("不能构成三角形")

if __name__ == '__main__':
    main()

