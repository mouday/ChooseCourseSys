
# 处理高层业务逻辑

class Education(object):
    def __init__(self, name):
        self.name = name

    def show_info(self):
        pass

    def __str__(self):
        return self.name

class School(Education, object):
    """学校"""
    def __init__(self, name, address):
        super(School, self).__init__(name)
        self.address = address
        self.teachers = []
        self.students = []
        self.courses = []
        self.grades = []
        print("school: %s create successful" % name)

    def enroll(self,student):# 学员注册
        self.students.append(student)
        print("%s enroll in %s "% (student.name, self.name))

    def leave_school(self,student): # 退学
        self.students.remove(student)
        print("%s leave school from %s " % (student.name, self.name))

    # 6.3 管理视图，创建讲师， 创建班级，创建课程
    def create_course(self, name, cycle, price):
        """3. 课程包含，周期，价格，通过学校创建课程"""
        course = Course(name, cycle, price)
        self.courses.append(course)
        print("course: %s create successful" % name)
        return course

    def create_teacher(self, name):
        teacher = Teacher(name, self)
        self.teachers.append(teacher)
        print("teacher: %s create successful" % name)
        return teacher

    def hire_teacher(self, teacher):
        self.teachers.append(teacher)
        print("teacher: %s hire successful" % teacher.name)

    def fire_teacher(self, teacher):
        self.teachers.remove(teacher)
        print("teacher: %s fired from %s" % (teacher.name, self.name))

    def create_grade(self, name, teacher, course):
        """4. 通过学校创建班级， 班级关联课程、讲师"""
        grade = Grade(name, teacher, course)
        self.grades.append(grade)
        print("grade: %s create successful" % name)
        return grade

class Grade(Education, object):
    """班级"""
    def __init__(self, name, teacher, course):
        super(Grade, self).__init__(name)
        self.teacher = teacher
        self.course = course
        self.students = []

    def enroll(self, student):  # 学员注册
        self.students.append(student)
        print("%s enroll in %s " % (student.name, self.name))

    def leave_grade(self, student): # 学员离开
        self.students.remove(student)
        print("%s leave grade from %s " % (student.name, self.name))

    def show_info(self):
        print("grade:name: %s\t teacher:%s\t course:%s\t students:%s"%
              (self.name, self.teacher, self.course, self.students))

class Student(Education, object):
    """学生
    5. 创建学员时，选择学校，关联班级
    """
    def __init__(self, name, school, grade, score=0):
        super(Student, self).__init__(name)
        self.score = score
        self.school = None
        self.grade = None
        self.tuition = 0
        self.choose_school(school)
        self.choose_grade(grade)

    # 6.1 学员视图， 可以注册， 交学费， 选择班级，
    def choose_school(self, school):
        if self.school != None:
            self.school.leave_school(self)
        school.enroll(self)
        self.school = school

    def choose_grade(self,grade):
        if self.grade !=None:
            self.grade.leave_grade(self)
        grade.enroll(self)
        self.grade = grade

    def pay_tuition(self, money):
        self.tuition += money

    def show_info(self):
        print("student:name: %s\t school:%s\t grade:%s\t score:%s\t tuition:%s"%
              (self.name, self.school, self.grade, self.score, self.tuition))


class Teacher(Education, object):
    """老师
    5. 创建讲师角色时要关联学校，
    """
    def __init__(self, name, school):
        super(Teacher, self).__init__(name)
        self.school = None
        self.choose_school(school)
        self.grade = None

    # 6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级，
    # 查看班级学员列表 ， 修改所管理的学员的成绩
    def choose_school(self, school):
        if self.school != None:
            self.school.fire_teacher(self)
        school.hire_teacher(self)
        self.school = school

    def choose_grade(self, grade):
        self.grade = grade

    def show_students(self):
        if self.grade != None:
            for student in self.grade.students:
                student.show_info()
        else:
            print("请选择班级")

    def modify_score(self, student, score):
        student.score = score

    def show_info(self):
        print("teacher:name: %s\t school:%s\t grade:%s"%
              (self.name, self.school, self.grade))

class Course(Education, object):
    """课程
    3. 课程包含，周期，价格，通过学校创建课程"""
    def __init__(self, name, cycle, price):
        super(Course, self).__init__(name)
        self.cycle = cycle
        self.price = price


if __name__ == "__main__":
    school = School("武汉大学","湖北")
    teacher= school.create_teacher("王老师")
    course = school.create_course("数学", "1年", 2000)
    grade = school.create_grade("高三", teacher,course)
    student = Student("Tom", school, grade)
    student.show_info()
    teacher.modify_score(student, 70)
    teacher.show_info()
    student.show_info()
