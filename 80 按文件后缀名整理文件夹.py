"""
Date:2026/5/12 10:47
Author:Jesse

Python入门习题第80练：按文件后缀名整理文件夹
需求：编写一个程序，用于遍历指定目录下的所有文件，并根据每个文件的后缀名进行分类。
"""
import os   #导入os模块,用于操作文件和目录
import shutil

#设置要操作的目录名称
dir = r"D:\python\python练习300题\arrange_dir"

#遍历指定目录下的所有文件和文件夹
for file in os.listdir(dir):
    # print("文件名",file)
    #获取文件后缀名
    ext = os.path.splitext(file)[1]
    #去除后缀名中的.
    ext = ext[1:]
    # print("后缀名",ext)

    #判断是否不存在以扩展名命名的文件夹
    if not os.path.isdir(f"{dir}/{ext}"):
        #创建以扩展名命名的文件夹
        os.mkdir(f"{dir}/{ext}")

    #构造源文件的完整路径
    source_path = f"{dir}/{file}"

    #构造目标文件的完整路径
    target_path = f"{dir}/{ext}/{file}"

    #移动文件到目标文件夹
    shutil.move(source_path,target_path)








