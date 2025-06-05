def display_beverages(beverages):
    """显示所有可售饮品信息"""
    print("欢迎光临！本店提供以下饮品：")
    print("------------------------------------")
    print("编号 | 名称        | 价格 (元)")
    print("------------------------------------")
    for code, info in beverages.items():
        print(f"{code:<4} | {info['name']:<10} | {info['price']:.2f}")
    print("------------------------------------")

def select_beverages(beverages):
    """用户选择饮品并返回选择列表和总价"""
    selected_items = []
    total_cost = 0
    while True:
        choice = input("请输入您想购买的饮品编号 (输入 '0' 完成选择): ")
        if choice == '0':
            break
        if choice in beverages:
            item = beverages[choice]
            selected_items.append(item['name'])
            total_cost += item['price']
            print(f"已添加 {item['name']} 到购物车。当前总额: {total_cost:.2f} 元")
        else:
            print("无效的饮品编号，请重新输入。")
    return selected_items, total_cost

def process_payment(total_cost):
    """处理支付过程"""
    if total_cost == 0:
        print("您没有选择任何饮品。")
        return False

    print(f"\n您需要支付的总金额为: {total_cost:.2f} 元")
    while True:
        try:
            payment_method = input("请选择支付方式 (1-投币, 2-扫码): ")
            if payment_method == '1':
                amount_paid = float(input(f"请投入 {total_cost:.2f} 元: "))
                if amount_paid >= total_cost:
                    change = amount_paid - total_cost
                    if change > 0:
                        print(f"支付成功！找零: {change:.2f} 元。")
                    else:
                        print("支付成功！")
                    return True
                else:
                    print(f"投入金额不足，还差 {total_cost - amount_paid:.2f} 元。请重新支付。")
            elif payment_method == '2':
                print("请扫描屏幕上的二维码进行支付...")
                # 模拟扫码支付成功
                input("支付完成后请按 Enter键...")
                print("支付成功！")
                return True
            else:
                print("无效的支付方式，请重新选择。")
        except ValueError:
            print("输入金额无效，请重新输入。")

def dispense_beverages(selected_items):
    """出货"""
    if selected_items:
        print("\n正在出货，请在出货口取走您的饮品：")
        for item_name in selected_items:
            print(f"- {item_name}")
        print("感谢您的购买！")

# 主程序
if __name__ == "__main__":
    # 饮品信息：编号 -> {名称, 价格}
    available_beverages = {
        "1": {"name": "可乐", "price": 3.00},
        "2": {"name": "雪碧", "price": 3.00},
        "3": {"name": "橙汁", "price": 3.50},
        "4": {"name": "矿泉水", "price": 2.00},
        "5": {"name": "咖啡", "price": 5.00},
        "6": {"name": "奶茶", "price": 4.50},
    }

    display_beverages(available_beverages)
    selected, total = select_beverages(available_beverages)

    if selected:
        if process_payment(total):
            dispense_beverages(selected)
    else:
        print("期待您的下次光临！")