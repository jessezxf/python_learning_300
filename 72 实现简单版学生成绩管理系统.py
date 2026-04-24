"""
Date:2026/4/23 16:35
Author:Jesse

Python入门习题第72练：实现简单版学生成绩管理系统
需求：实现一个简单的学生成绩管理系统。这个系统允许我们添加学生、记录学生成绩，并计算每个学生的平均成绩。
"""

#定义学生类
class Student:
    """用于表示一个学生及其成绩列表"""
    def __init__(self,name):
        self.name = name
        self.grades = []        #学生成绩列表，初始化为空

    def add_grade(self,grade):
        """
        添加成绩到学生成绩列表
        :param grade:
        :return: 无
        """
        self.grades.append(grade)

    def average_grade(self):
        """
        计算学生平均成绩
        参数：无
        :return:平均成绩，0（没有成绩）
        """
        #判断是否没有成绩
        if self.grades == 0:
            #返回0，并结束方法运行
            return 0
        #返回平均成绩
        return sum(self.grades) / len(self.grades)




class StudentGradeManager:
    """用于管理学生及其成绩"""
    def __init__(self):
        """初始化学生成绩管理对象"""
        self.students = {}  # 存储学生及其成绩的字典,键为学生姓名


    def add_student(self,name):
        """
        添加学生
        :param name:
        :return:无
        """
        #判断学生是否存在
        if name not in self.students:
            #添加学生到列表
            self.students[name] = Student(name)


        else:
            print(f"学生{name}已存在！！")

    def get_student(self,name):
        """
        通过名称查找学生
        :param name: 要查找的学生姓名
        :return: student（学生对象）或None（没有找到）
        """
        return self.students.get(name)
















