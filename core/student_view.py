
""" # 6.1学员视图， 可以注册， 交学费， 选择班级，选择学校"""

import os
import sys

# 导入路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from core import education
from core import data

def add_student():
    print("请填写学生信息：")
    name = input("姓名：")

    print("选择学校：")
    data.print_schools()
    school_name = input("学校名：")
    school = data.get_school(school_name)
    if school == None:
        print("学校选择错误")
        return

    print("选择班级：")
    data.print_grades()
    grade_name = input("班级名：")
    grade = data.get_grade(grade_name)
    if grade == None:
        print("班级选择错误")
        return

    student = education.Student(name, school, grade)
    data.update_student(student)
    data.update_school(school)
    data.update_grade(grade)

def pay_tuition():

    print("选择学生：")
    data.print_students()
    student_name = input("学生名：")
    student = data.get_student(student_name)
    if student == None:
        print("学生选择错误")
        return

    money =  input("请输入学费金额：")
    if not money.isdigit():
        print("输入金额不正确")
        return

    student.pay_tuition(int(money))
    data.update_student(student)

def choose_grade():
    print("选择学生：")
    data.print_students()
    student_name = input("学生名：")
    student = data.get_student(student_name)
    if student == None:
        print("学生选择错误")
        return

    print("选择班级：")
    data.print_grades()
    grade_name = input("班级名：")
    grade = data.get_grade(grade_name)
    if grade == None:
        print("班级选择错误")
        return

    student.choose_grade(grade)
    data.update_student(student)
    data.update_grade(grade)

def choose_school():
    print("选择学生：")
    data.print_students()
    student_name = input("学生名：")
    student = data.get_student(student_name)
    if student == None:
        print("学生选择错误")
        return

    print("选择学校：")
    data.print_schools()
    school_name = input("学校名：")
    school = data.get_school(school_name)
    if school == None:
        print("学校选择错误")
        return

    student.choose_school(school)
    data.update_student(student)
    data.update_school(school)

def show_student():
    print("选择学生：")
    data.print_students()
    student_name = input("学生名：")
    student = data.get_student(student_name)
    if student == None:
        print("学生选择错误")
        return
    student.show_info()

def show_students():
    data.print_students()

def run():
    print("学生视图：")
    print("=" * 20)
    while True:
        print("1.增加学生\n2.交学费\n3.选择班级\n4.选择学校\n"
              "5.查看学生\n6.查看详细\n"
              "0.退出")
        res = input("输入序号：")

        if res == "1":
            add_student()
        elif res == "2":
            pay_tuition()
        elif res == "3":
            choose_grade()
        elif res == "4":
            choose_school()
        elif res == "5":
            show_students()
        elif res == "6":
            show_student()
        elif res == "0":
            print("退出成功！")
            break
        else:
            print("请选择正确的编号")


if __name__ == "__main__":
    run()