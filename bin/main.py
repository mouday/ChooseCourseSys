
# 系统入口

import os
import sys

# 导入路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

# 导入核心包

from core import school_view
from core import teacher_view
from core import student_view

def main():
    choice = input("请选择角色：0.学校，1.教师，2.学生")
    if choice == "0":
        school_view.run()
    elif choice == "1":
        teacher_view.run()
    elif choice == "2":
        student_view.run()
    else:
        print("角色选择失败")

if __name__ == "__main__":
    main()