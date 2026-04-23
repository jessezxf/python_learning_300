"""
Date:2026/4/22 10:26
Author:Jesse

Python入门习题第68练：定义学生类
需求：定义一个学生类，用于存储学生的基本信息（如姓名、年龄、学号），并提供查询这些信息的方法。
"""
# 定义学生类
class Student:
    """
    存储学生的基本信息
    """
    def __init__(self,name,age,sid):
        """初始化学生对象"""
        self.name = name
        self.age = age
        self.sid = sid

    def get_name(self):
        """
        获取学生姓名
        :return:self.name(学生姓名)
        """
        return self.name

    def get_age(self):
        """
        获取学生年龄
        :return:self.age(学生年龄)
        """
        return self.age

    def get_sid(self):
        """
        获取学生学号
        :return:self.sid(学生学号)
        """
        return self.sid







#示例使用，实例化对象
student = Student("Jesse",18,"001")


#获取学生姓名
print(student.get_name())








