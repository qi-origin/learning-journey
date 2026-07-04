# 函数与列表/字典配合
def find_student(students,name):
    """在列表中查找学生，找到返回字典，找不到返回 None"""
    for student in students:
        if student["name"]==name:
            return student
        else :
            return None
        
student_list={
    {"name":"张三","score":85},
    {"name":"李四","score":98}
}
result=find_student(student_list,"李四")
if result:
    print(f"{result["name"]}的成绩是{result["score"]}")
else:
    print("未找到")



#检验自己：写一个函数 add_student(students, name, score)，往列表里添加学生字典，并返回更新后的列表。
def add_student(students,name,score):
    """该函数用于往学生列表里添加学生字典，并返回更新后的列表。"""
    new_student={"name":name,"score":score}
    students.append(new_student)
    return students
