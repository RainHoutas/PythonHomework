class Course:
    def __init__(self, number, name, teacher, location):
        self.number = number
        self.name = name
        self.teacher = teacher
        self.__location = location  # 私有属性

    def show_info(self):
        """显示课程信息"""
        print(f"课程编号: {self.number}")
        print(f"课程名称: {self.name}")
        print(f"任课教师: {self.teacher}")
        print(f"上课地点: {self.__location}") # 在类内部可以访问私有属性

# 创建Course类的对象
math_course = Course("CS101", "高等数学", "王老师", "教学楼A栋101")

# 显示课程信息
math_course.show_info()
