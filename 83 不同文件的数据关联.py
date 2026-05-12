"""
Date:2026/5/12 15:58
Author:Jesse

Python入门习题第83练：不同文件的数据关联
需求：编写一个程序，从course_teacher.txt和course_student_grade.txt两个文本文件中读取信息，
并打印出包含课程名称、教师姓名、学生学号、学生姓名和学生成绩的完整信息。
"""

#定义字典保存课程和教师之间的映射关系
course_teacher = {}

#读取文件内容
with open('course_teacher.txt','r',encoding='utf-8') as f:
    #遍历文件的每一行
    for line in f.readlines():
        #去除每一行的换行符
        line = line[:-1]

        course,teacher = line.split(',')
        #将课程和教师之间的映射关系保存到字典中
        course_teacher[course] = teacher


#读取文件内容
with open('course_student_grade.txt','r',encoding='utf-8') as f:
    # 遍历文件的每一行
    for line in f.readlines():
        # 去除每一行的换行符
        line = line[:-1]
        course,stuid,name,grade = line.split(',')
        # print(course,stuid,name,grade)

        #从字典中获取对应课程的教师姓名
        teacher = course_teacher[course]
        #打印完整信息
        print(course,teacher,stuid,name,grade)













