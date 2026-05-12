"""
Date:2026/5/12 11:39
Author:Jesse

Python入门习题第81练：递归搜索目录找出最大文本文件
需求：编写一个程序，搜索指定目录（含其子目录）内的所有.txt文件，并找出其中最大的文件及其大小。
"""
import os   #导入os模块,用于操作文件和目录

#设置要搜索的目录路径
search_dir = r"D:\python\python练习300题"

#定义列表保存找到的文件及其大小
result_files = []

for root,dir,files in os.walk(search_dir):
    # print(root,dir,files)

    #遍历当前目录下的所有文件
    for file in files:
        #判断文件是否以.txt结尾
        if file.endswith(".txt"):
            #构造文件的完整路径
            file_path = f"{root}/{file}"
            #获取文件的大小
            file_size = os.path.getsize(file_path)

            #将文件路径和大小作为一个元组添加到列表中
            result_files.append((file_path,file_size))



#对列表中的元组按照文件大小进行排序
sorted_file = sorted(result_files,key=lambda x:x[1],reverse=True)

#打印排序后的第一个元素，最大的文件路径和大小
print(sorted_file[0])















