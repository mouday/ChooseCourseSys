
# 处理数据存储与提取，实现增删改查

import pickle

path = "../datas/data.pk"  # 数据路径

def dump(obj):
    f = open(path, "wb")
    pickle.dump(obj, f)
    f.close()

def load():
    f=  open(path, "rb")
    infos = pickle.load(f)
    f.close()
    return infos

# 打印数据信息
def print_all_infos():
    infos = load()
    print("=" * 50)
    for key in infos:
        print(key,":")
        for key2 in infos.get(key):
            print("\t",key2, ":", infos.get(key).get(key2))
    print("=" * 50)

def print_infos(key):
    infos = load()
    print(key.center(50, "="))
    print("\t", "名称", ":", "对象")
    print("\t", "-"*30)
    for key2 in infos.get(key):
        print("\t", key2, ":", infos.get(key).get(key2))
    print("=" * 50)

def print_schools():
    key = "schools"
    print_infos(key)

def print_teachers():
    key = "teachers"
    print_infos(key)

def print_students():
    key = "students"
    print_infos(key)

def print_courses():
    key = "courses"
    print_infos(key)

def print_grades():
    key = "grades"
    print_infos(key)

# 查询
def get_infos(class_name):
    infos = load()
    return infos.get(class_name)

# 查询学校
def get_schools():
    return get_infos("schools")

def get_school(school_name):
    return get_schools().get(school_name)

# 查询老师
def get_teachers():
    return get_infos("teachers")

def get_teacher(teacher_name):
    return get_teachers().get(teacher_name)

# 查询学生
def get_students():
    return get_infos("students")

def get_student(student_name):
    return get_students().get(student_name)

# 查询班级
def get_grades():
    return get_infos("grades")

def get_grade(grade_name):
    return get_grades().get(grade_name)

# 查询课程
def get_courses():
    return get_infos("courses")

def get_course(course_name):
    return get_courses().get(course_name)

# 修改
def update(dct):
    obj = load()
    obj.update(dct)
    dump(obj)

def update_school(school):
    infos=load()
    infos["schools"].update({school.name:school})
    dump(infos)

def update_teacher(teacher):
    infos=load()
    infos["teachers"].update({teacher.name:teacher})
    dump(infos)

def update_student(student):
    infos=load()
    infos["students"].update({student.name:student})
    dump(infos)

def update_course(course):
    infos=load()
    infos["courses"].update({course.name:course})
    dump(infos)

def update_grade(grade):
    infos=load()
    infos["grades"].update({grade.name:grade})
    dump(infos)


def init():
    # 存储结构：
    infos = {
        "schools": {
            # "school_name": "school_obj"
        },
        "teachers": {
            # "teacher_name": "teacher_obj"
        },
        "students": {
            # "student_name": "student_obj"
        },
        "grades": {
            # "grade_name": "grade_obj"
        },
        "courses": {
            # "course_name": "course_obj"
        }
    }
    # 初始化数据
    res = input("是否初始化数据？（y）:")
    if res == "y":
        dump(infos)
        print("数据初始化成功！")
    else:
        print("数据初始化失败！")

if __name__ == '__main__':
    init()