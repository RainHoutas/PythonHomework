class jisuan:
    def duochengji(*q):
        result = 1
        for i in q:
            result *= i
        return result

xinjisuan = jisuan()

print(jisuan.duochengji(2,3,4,5))

#先定义一个类，里面有一个方法，方法可以接收任意数量的参数，然后返回这些参数的乘积