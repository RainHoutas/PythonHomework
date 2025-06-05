from datetime import datetime, date

class Medicine:
    def __init__(self, name, price, pd_str, exp_str):
        self.name = name
        self.__price = price  # 私有属性
        try:
            # 将字符串日期转换为date对象
            self.__pd = datetime.strptime(pd_str, "%Y-%m-%d").date()
            self.__exp = datetime.strptime(exp_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("日期格式不正确，应为 YYYY-MM-DD")

    def get_price(self):
        """获取药品价格"""
        return self.__price

    def get_pd(self):
        """获取生产日期"""
        return self.__pd

    def get_exp(self):
        """获取失效日期"""
        return self.__exp

    def guarantee_period(self):
        """计算保质期（天数）"""
        if self.__exp and self.__pd:
            period = self.__exp - self.__pd
            return period.days
        return None

    def is_expire(self):
        """计算药品是否过期"""
        if self.__exp:
            today = date.today()
            return today > self.__exp
        return None # 如果没有失效日期，无法判断

# 创建Medicine类的实例对象
try:
    aspirin = Medicine("阿司匹林", 15.50, "2023-01-15", "2025-01-14")

    print(f"药品名称: {aspirin.name}")
    print(f"药品价格: {aspirin.get_price()} 元")
    print(f"生产日期: {aspirin.get_pd()}")
    print(f"失效日期: {aspirin.get_exp()}")

    shelf_life = aspirin.guarantee_period()
    if shelf_life is not None:
        print(f"保质期: {shelf_life} 天")
    else:
        print("无法计算保质期。")

    if aspirin.is_expire():
        print("药品已过期。")
    elif aspirin.is_expire() is False: # 明确判断 False，因为可能返回 None
        print("药品未过期。")
    else:
        print("无法判断药品是否过期。")

    print("\n---尝试创建日期格式错误的药品---")
    invalid_medicine = Medicine("无效药品", 10.0, "2023/12/01", "2024/12/01")

except ValueError as e:
    print(f"错误: {e}")

print("\n---尝试创建已过期的药品---")
try:
    expired_medicine = Medicine("过期感冒药", 20.0, "2020-01-01", "2022-01-01")
    print(f"药品名称: {expired_medicine.name}")
    if expired_medicine.is_expire():
        print("药品已过期。")
    else:
        print("药品未过期。")
except ValueError as e:
    print(f"错误: {e}")