def count_words_in_file(filename):
    # 1. 初始化单词总数为 0
    total_words = 0
    try:
        # 2. 使用 with 语句打开文件，它会自动关闭文件
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                # 将行分割成单词列表
                word_in_line = line.split()
                # 累加单词数量
                total_words += len(word_in_line)
    except FileNotFoundError:
        # 增加一个错误处理，防止文件不存在时程序崩溃
        print(f"错误：文件 '{filename}' 未找到。")
        return 0

    # 3. 返回最终统计的总数
    return total_words

# --- 测试代码 ---
# 假设已经存在一个名为 'article.txt' 的文件
# file_path = 'article.txt'
# word_count = count_words_in_file(file_path)
# print(f"文件 '{file_path}' 中的总单词数是: {word_count}")