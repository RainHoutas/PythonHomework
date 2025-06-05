def fibonacci(n):
    """
    使用递归计算斐波纳契数列的第n项。

    参数:
    n (int): 要计算的斐波纳契数列的项数 (n>=0)。

    返回:
    int: 斐波纳契数列的第n项的值。
    """
    if n < 0:
        raise ValueError("输入必须是非负整数")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 获取用户输入
try:
    num = int(input("请输入一个非负整数 n: "))
    result = fibonacci(num)
    print(f"斐波纳契数列的第 {num} 项是: {result}")
except ValueError as e:
    print(e)
except RecursionError:
    print(f"计算 F({num}) 超出了最大递归深度。对于较大的 n，递归方法效率较低。")