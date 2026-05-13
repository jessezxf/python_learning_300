"""
Date:2026/5/13 10:59
Author:Jesse

Python入门习题第89练：CSV文件备份
需求：从人员信息.csV文件中读取内容，并将其完整复制到另一个CSV文件中。
"""

import csv

#读取文件内容
with open('人员信息_89.csv','r',encoding='utf-8') as f:
    reader = csv.reader(f)
    #将每一行保存到data列表中
    data = [row for row in reader]

#往新文件中写入内容
with open('人员信息备份_89.csv','w',encoding='utf-8',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)





