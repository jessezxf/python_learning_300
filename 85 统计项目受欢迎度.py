"""
Date:2026/5/12 17:20
Author:Jesse

Python入门习题第85练：统计项目受欢迎度
需求：从student_like.txt文件中读取学生喜欢的项目列表，并统计各个项目的受欢迎程度（即被多少学生喜欢）。
"""
#定义字典保存每个项目的名称及其受欢迎程度
like_count = {}


#读取文件内容
with open('student_like.txt', 'r', encoding='utf-8') as f:
    #遍历文件的每一行
    for line in f.readlines():
        #去除每一行末尾的换行符
        line = line.strip()
        #将每一行按空格分割成列表
        name,likes = line.split(" ")
        # print(name,likes)
        #将喜欢的项目按逗号分割成列表
        like_list = likes.split(",")
        # print(like_list)
        #遍历喜欢的项目列表
        for like in like_list:
            #如果项目名称不在字典中，则添加到字典中，并将值设为1
            if like not in like_count:
                like_count[like] = 1
            #如果项目名称在字典中，则将值加1
            else:
                like_count[like] += 1

print(like_count)