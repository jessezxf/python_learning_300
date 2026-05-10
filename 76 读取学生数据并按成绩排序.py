"""
Date:2026/5/10 17:33
Author:Jesse

Python入门习题第76练：读取学生数据并按成绩排序
需求：从students_grade_file.txt文件中读取学生数据（学号、姓名、成绩），并根据成绩进行排序。
"""
#定义函数
def read_file():
    """
    读取文件内容
    :return:学生数据列表，每一个元素是一个包含学号、姓名、成绩的列表
    """
    #定义一个空列表，用于存储学生数据
    result = []

    #读取文件内容
    with open("students_grade_file.txt","r",encoding="utf-8") as f:
        #遍历文件的每一行
        for line in f.readlines():
            #去除每行末尾的换行符
            line = line[:-1]
            #将每行内容按逗号分隔
            line = line.split(",")
            #将每行内容添加到结果列表中
            result.append(line)

    #返回包含所有学生数据的列表
    return result

def sort_grade(data):
    """
    对学生数据进行排序
    :param data:学生数据列表，每一个元素是一个包含学号、姓名、成绩的列表
    :return:排序后的学生数据列表
    """
    #对数据进行排序
    return sorted(data,key=lambda x: int(x[2]), reverse=True)

def write_file(data):
    """
    将排序后的数据写入文件
    :param data:排序后的学生数据列表
    :return:None
    """
    #打开文件
    with open("students_grade_sort_file.txt","w",encoding="utf-8") as f:
        #遍历排序后的数据列表
        for d in data:
            # print(d)

            #str.jion(序列)：将序列中的元素以指定的字符串连接成一个新的字符串
            # print(".".join(["123","456","789"]))

            #将子列表转换为逗号分隔的字符串，并写入文件
            f.write(",".join(d) + "\n")

#读取文件内容
data = read_file()
# print("读取文件内容",data)

#对数据进行排序
data = sort_grade(data)
# print("成绩排序后的内容",data)

#将排序后的数据写入xin文件
write_file(data)







