class Student:
    def __init__(self, name, chinese_score, math_score, physics_score):
        self.name = name
        self.chinese_score = chinese_score
        self.math_score = math_score
        self.physics_score = physics_score

    def __add__(self, other):
        """重载+运算符，用于合并两个学生对象的成绩"""
        if not isinstance(other, Student):
            return NotImplemented # 或者抛出 TypeError

        total_chinese = self.chinese_score + other.chinese_score
        total_math = self.math_score + other.math_score
        total_physics = self.physics_score + other.physics_score
        # 新的学生对象名称可以自定义，这里简单地将两个名字合并
        return Student(f"{self.name}+{other.name}", total_chinese, total_math, total_physics)

    def __str__(self):
        return (f"学生: {self.name}, 语文: {self.chinese_score}, "
                f"数学: {self.math_score}, 物理: {self.physics_score}")

# 创建学生对象
student1 = Student("张三", 85, 90, 78)
student2 = Student("李四", 92, 88, 95)
student3 = Student("王五", 79, 85, 80)

print("学生信息:")
print(student1)
print(student2)
print(student3)

# 成绩求和
# 两个学生成绩求和
sum_s1_s2 = student1 + student2
print(f"\n{student1.name} 和 {student2.name} 的成绩总和:")
print(sum_s1_s2)

# 多个学生成绩求和
all_students = [student1, student2, student3]
if all_students:
    total_scores_student = Student("总计", 0, 0, 0) # 用于累加的初始学生对象
    for student in all_students:
        total_scores_student.chinese_score += student.chinese_score
        total_scores_student.math_score += student.math_score
        total_scores_student.physics_score += student.physics_score
    total_scores_student.name = "所有学生总分"

    print("\n所有学生成绩总和:")
    print(total_scores_student)

    num_students = len(all_students)
    if num_students > 0:
        avg_chinese = total_scores_student.chinese_score / num_students
        avg_math = total_scores_student.math_score / num_students
        avg_physics = total_scores_student.physics_score / num_students

        print("\n各科平均分:")
        print(f"语文平均分: {avg_chinese:.2f}")
        print(f"数学平均分: {avg_math:.2f}")
        print(f"物理平均分: {avg_physics:.2f}")
else:
    print("\n没有学生数据可供计算。")