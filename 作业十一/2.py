list01 = ["study", "Python", "strong", "smart", "beautiful"]

# 将列表中的所有元素转换为首字母大写的形式
title_cased_list = [s.title() for s in list01]
# 然后对转换后的列表进行排序
sorted_title_cased_list = sorted(title_cased_list)

print(f"原始列表: {list01}")
print(f"转换为首字母大写并排序后的列表: {sorted_title_cased_list}")