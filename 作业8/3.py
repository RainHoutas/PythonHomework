# 学生信息列表
students = []

def display_menu():
    """显示功能菜单"""
    print("\n欢迎使用学生管理系统")
    print("-----------------------------------")
    print("1. 添加学生信息")
    print("2. 删除学生信息")
    print("3. 修改学生信息")
    print("4. 查询学生信息")
    print("5. 退出系统")
    print("-----------------------------------")

def find_student_by_id(student_id):
    """根据学生ID查找学生及其在列表中的索引"""
    for index, student in enumerate(students):
        if student['id'] == student_id:
            return student, index
    return None, -1

def add_student():
    """添加学生信息"""
    print("\n--- 添加学生信息 ---")
    student_id = input("请输入学生ID: ")
    _ , index = find_student_by_id(student_id)
    if index != -1:
        print(f"错误：ID为 {student_id} 的学生已存在！")
        return

    name = input("请输入学生姓名: ")
    while True:
        try:
            age = int(input("请输入学生年龄: "))
            if age <= 0:
                print("年龄必须是正整数。")
            else:
                break
        except ValueError:
            print("输入无效，年龄必须是数字。")

    students.append({'id': student_id, 'name': name, 'age': age})
    print("学生信息添加成功！")

def delete_student():
    """删除学生信息"""
    print("\n--- 删除学生信息 ---")
    student_id = input("请输入要删除的学生ID: ")
    student, index = find_student_by_id(student_id)

    if student:
        confirm = input(f"确定要删除学生 {student['name']} (ID: {student_id})吗? (y/n): ").lower()
        if confirm == 'y':
            students.pop(index)
            print("学生信息删除成功！")
        else:
            print("已取消删除操作。")
    else:
        print(f"未找到ID为 {student_id} 的学生。")

def modify_student():
    """修改学生信息"""
    print("\n--- 修改学生信息 ---")
    student_id = input("请输入要修改的学生ID: ")
    student, index = find_student_by_id(student_id)

    if student:
        print(f"当前信息: ID: {student['id']}, 姓名: {student['name']}, 年龄: {student['age']}")
        new_name = input(f"请输入新的姓名 (原姓名: {student['name']}, 直接回车不修改): ")
        while True:
            new_age_str = input(f"请输入新的年龄 (原年龄: {student['age']}, 直接回车不修改): ")
            if not new_age_str: # 用户直接回车
                new_age = student['age']
                break
            try:
                new_age = int(new_age_str)
                if new_age <= 0:
                    print("年龄必须是正整数。")
                else:
                    break
            except ValueError:
                print("输入无效，年龄必须是数字。")

        if new_name:
            students[index]['name'] = new_name
        students[index]['age'] = new_age
        print("学生信息修改成功！")
        print(f"更新后信息: ID: {students[index]['id']}, 姓名: {students[index]['name']}, 年龄: {students[index]['age']}")
    else:
        print(f"未找到ID为 {student_id} 的学生。")

def query_student():
    """查询学生信息"""
    print("\n--- 查询学生信息 ---")
    if not students:
        print("系统中没有任何学生信息。")
        return

    query_id = input("请输入要查询的学生ID (直接回车查询所有学生): ")

    if not query_id: # 查询所有学生
        print("\n所有学生信息如下:")
        print("-----------------------------------")
        print(f"{'ID':<10} | {'姓名':<15} | {'年龄':<5}")
        print("-----------------------------------")
        for student in students:
            print(f"{student['id']:<10} | {student['name']:<15} | {student['age']:<5}")
        print("-----------------------------------")
    else: # 按ID查询单个学生
        student, _ = find_student_by_id(query_id)
        if student:
            print("\n查询结果:")
            print("-----------------------------------")
            print(f"{'ID':<10} | {'姓名':<15} | {'年龄':<5}")
            print("-----------------------------------")
            print(f"{student['id']:<10} | {student['name']:<15} | {student['age']:<5}")
            print("-----------------------------------")
        else:
            print(f"未找到ID为 {query_id} 的学生。")

def main():
    """主函数，程序入口"""
    while True:
        display_menu()
        choice = input("请输入您的选择 (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            delete_student()
        elif choice == '3':
            modify_student()
        elif choice == '4':
            query_student()
        elif choice == '5':
            print("感谢使用学生管理系统，再见！")
            break
        else:
            print("无效的选择，请输入1到5之间的数字。")
        input("\n按任意键返回主菜单...") # 暂停，等待用户按键

if __name__ == "__main__":
    main()