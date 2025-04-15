
students = {}


n = int(input("Enter the number of students: "))
for _ in range(n):
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    students[student_id] = student_name


print("\nStudent Information (sorted by ID):")
for student_id in sorted(students.keys()):
    print(f"ID: {student_id}, Name: {students[student_id]}")