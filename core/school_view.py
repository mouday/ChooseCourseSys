
""" 6.3管理视图，创建讲师， 创建班级，创建课程"""

import os
import sys

# 导入路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from core import education
from core import data

# 创建班级
def add_grade():
    print("请填写班级信息：")
    grade_name = input("名称：")

    print("选择学校：")
    data.print_schools()
    school_name = input("学校名：")
    school = data.get_school(school_name)
    if school == None:
        print("学校选择错误")
        return

    print("选择老师：")
    data.print_teachers()
    teacher_name = input("老师名：")
    teacher = data.get_teacher(teacher_name)
    if teacher == None:
        print("老师选择错误")
        return

    print("选择课程：")
    data.print_courses()
    course_name = input("课程名：")
    course = data.get_course(course_name)
    if course == None:
        print("课程选择错误")
        return

    grade = school.create_grade(grade_name, teacher, course)
    data.update_grade(grade)
    data.update_school(school)

# 创建学校
def add_school():
    print("请填写学校信息：")
    school_name = input("名称：")
    address = input("地址：")

    school = education.School(school_name, address)
    data.update_school(school)

# 创建课程:linux , python , go 3个  linux\py 在北京开， go 在上海开
def add_course():
    print("请填写课程信息：")
    course_name = input("名称：")
    cycle = input("周期：")
    price = input("学费：")

    print("选择学校：")
    data.print_schools()
    school_name = input("学校名：")
    school = data.get_school(school_name)
    if school == None:
        print("学校选择错误")
        return

    course = school.create_course(course_name, cycle, price)
    data.update_course(course)
    data.update_school(school)

# 创建老师
def add_teacher():
    print("请填写教师信息：")
    teacher_name = input("姓名：")

    print("选择学校：")
    data.print_schools()
    school_name = input("学校名：")
    school = data.get_school(school_name)
    if school == None:
        print("学校选择错误")
        return

    teacher = school.create_teacher(teacher_name)
    data.update_teacher(teacher)
    data.update_school(school)
    print("老师 %s 创建成功！"% teacher.name)

def show_schools():
    data.print_schools()

def show_courses():
    data.print_courses()

def show_teachers():
    data.print_teachers()

def show_grades():
    data.print_grades()

def show_teacher():
    print("选择老师：")
    data.print_teachers()
    teacher_name = input("老师名：")
    teacher = data.get_teacher(teacher_name)
    if teacher == None:
        print("老师选择错误")
        return

    teacher.show_info()

def run():
    print("学校视图：")
    print("=" * 20)
    while True:
        print("1.增加学校\n2.增加老师\n3.增加课程\n4.增加班级\n"
              "5.查看学校\n6.查看老师\n7.查看课程\n8.查看班级\n"
              "9.查看教师详细\n"
              "0.退出")
        res = input("输入序号：")

        if res == "1":
            add_school()
        elif res == "2":
            add_teacher()
        elif res == "3":
            add_course()
        elif res == "4":
            add_grade()
        elif res == "5":
            show_schools()
        elif res == "6":
            show_teachers()
        elif res == "7":
            show_courses()
        elif res == "8":
            show_grades()
        elif res == "9":
            show_teacher()
        elif res == "0":
            print("退出成功！")
            break
        else:
            print("请选择正确的编号")


if __name__ == "__main__":
    run()