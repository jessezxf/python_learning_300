"""
Date:2026/5/12 15:31
Author:Jesse

Python入门习题第82练：统计课程最高分最低分平均分
需求：从course_student_grade.txt文件中读取课程和学生成绩信息，计算并打印出每门课程的最高分、最低分和平均分。
"""
#定义字典保存课程和学生成绩之间的映射关系
course_grade = {}


#读取文件内容
with open(r"D:\python\python练习300题\course_student_grade.txt", "r", encoding="utf-8") as f:
    #遍历文件内容
    for line in f.readlines():
        #去除换行符
        line = line[:-1]

        course,stuid,name,grade = line.split(",")
        #判断课程是否在字典中
        if course not in course_grade:
            #如果课程不在字典中，则添加课程并初始化为空列表
            course_grade[course] = []
        #将成绩添加到对应课程的列表中
        course_grade[course].append(float(grade))


#遍历字典的键值对
for course,grades in course_grade.items():
    print(course,max(grades),min(grades),sum(grades)/len(grades))












