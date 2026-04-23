"""
Date:2026/4/4 17:23
Author:Jesse

Python入门习题第10练：学生成绩排序
需求：给定一个学生信息列表，根据学生的成绩进行排序。
# 原始列表
students =[
{'sno':101, 'sname': "小张",'sgrade': 88},
{'sno':102,'sname':"小王",'sgrade': 77},
{'sno':103,'sname':"小李",'sgrade':99},
{'sno':104,'sname':"小赵",'sgrade': 66}
]
"""

students =[
{'sno':101, 'sname': "小张",'sgrade': 88},
{'sno':102,'sname':"小王",'sgrade': 77},
{'sno':103,'sname':"小李",'sgrade':99},
{'sno':104,'sname':"小赵",'sgrade': 66}
]
students_sort = sorted(students,key=lambda student:student['sgrade'])   #升序排列
students_sort = sorted(students,key=lambda student:student['sgrade'],reverse=True)      #降序排列

print(f'原列表：{students}')
print(f'排序后列表：{students_sort}')



