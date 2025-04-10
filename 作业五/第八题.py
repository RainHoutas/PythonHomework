# Initialize the product list and shopping cart
product_list = []
shopping_cart = []

# Step 1: Input 5 product details
for _ in range(5):
    product = input("请输入商品的编号和商品的名称进行商品入库，每次只能输入一件商品：")
    product_list.append(product)

# Display the product list
print("\n".join(product_list))

# Step 2: Allow the user to select products to add to the shopping cart
while True:
    product_id = input("请输入要购买的商品编号：")
    if product_id == "q":
        break
    # Check if the product exists in the product list
    selected_product = next((p for p in product_list if p.startswith(product_id)), None)
    if selected_product:
        shopping_cart.insert(0, selected_product)  # Add to the cart in reverse order
        print("商品己成功添加到购物车")
    else:
        print("该商品不存在！")

# Step 3: Display the shopping cart contents
print("您购物车里已选择的商品为：")
print("\n".join(shopping_cart))