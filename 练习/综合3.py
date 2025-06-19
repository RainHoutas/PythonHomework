def write_user_info(filename, user_list):
    """将用户信息写入文件。"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for username, password in user_list:
                f.write(f"{username}:{password}\n")
        print(f"用户信息已成功写入到 '{filename}'。")
    except IOError as e:
        print(f"写入文件时出错: {e}")

def read_user_info(filename):
    """从文件读取用户信息并返回字典。"""
    user_dict = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                # 去除行尾的换行符并按':'分割
                parts = line.strip().split(':')
                if len(parts) == 2:
                    username, password = parts
                    user_dict[username] = password
        print(f"用户信息已从 '{filename}' 读取。")
    except FileNotFoundError:
        print(f"错误: 文件 '{filename}' 未找到。")
    except IOError as e:
        print(f"读取文件时出错: {e}")
    return user_dict

# --- 测试代码 ---
# 准备用户数据
users_to_write = [('alice', '123456'), ('bob', 'abcdef'), ('charlie', 'qwerty')]

# 写入文件
file_path = 'users.txt'
write_user_info(file_path, users_to_write)

# 读取文件并打印结果
user_data = read_user_info(file_path)
print("\n从文件读取到的用户数据字典：")
print(user_data)