def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("请输入体重(kg): "))
height = float(input("请输入身高(m): "))
bmi = calculate_bmi(weight, height)
print(f"您的BMI指数为: {bmi}")