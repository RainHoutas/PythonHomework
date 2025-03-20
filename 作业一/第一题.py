def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

celsius = float(input("请输入摄氏温度(℃): "))
kelvin = celsius_to_kelvin(celsius)
print(f"对应的开氏温度为: {kelvin} K")