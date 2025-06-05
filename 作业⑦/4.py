def check_id(id_number):
    if len(id_number) != 18:
        print("身份证号码长度不正确!")
        return

    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_codes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

    try:
        sum_val = 0
        for i in range(17):
            sum_val += int(id_number[i]) * weights[i]
        remainder = sum_val % 11
        expected_check = check_codes[remainder]
    except ValueError:
        print("身份证字符不对")
        return

    if id_number[-1].upper() != expected_check:
        print("身份证校验位不对")
    else:
        year = id_number[6:10]
        month = id_number[10:12]
        day = id_number[12:14]
        gender_code = int(id_number[16])
        gender = "男" if gender_code % 2 == 1 else "女"
        print("身份证号码校验为合法号码!！！！！！！！！！！！！！！！！")
        print(f"出生：{year}年{month}月{day}日")
        print(f"性别：{gender}")


# 示例调用
check_id("432831196411150812")
check_id("432831456811150810")
check_id("350105199503333487")
