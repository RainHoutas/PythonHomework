def get_long_words(text):
    """
    从英文字符串中选出长度超过4的单词，并顺序返回。

    参数:
    text (str): 输入的英文字符串。

    返回:
    generator: 一个生成器，逐个产生长度超过4的单词。
    """
    if not isinstance(text, str):
        raise TypeError("输入必须是字符串")

    words = text.split()
    for word in words:
        # 简单地去除一些常见标点符号，以便更准确地判断单词长度
        cleaned_word = ''.join(filter(str.isalpha, word))
        if len(cleaned_word) > 4:
            yield cleaned_word  # 或者 yield word 如果希望保留原始标点


# 示例用法
my_string = "This is a sample sentence with some fairly long words like programming and Python."
print("长度超过4的单词:")
for long_word in get_long_words(my_string):
    print(long_word)

print("\n尝试非字符串输入:")
try:
    for lw in get_long_words(["not", "a", "string"]):
        print(lw)
except TypeError as e:
    print(f"错误: {e}")