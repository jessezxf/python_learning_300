"""
Date:2026/5/12 16:32
Author:Jesse

Python入门习题第84练：批量合并文本文件
需求：编写一个程序，用于将指定目录下所有，txt文件的内容合并到一个新的文件中，每个文件的内容之间使用换行符分隔。
"""
import os

#目标目录路径
data_dir = r"D:\python\python练习300题\datas\many_texts"
#定义列表保存文件内容
contents = []

#遍历目标目录下的所有文件和文件夹
for file in os.listdir(data_dir):
    #构建文件的完整地址
    file_path = f"{data_dir}/{file}"
    #判断是否为普通文件且为.txt文件
    if os.path.isfile(file_path) and file.endswith(".txt"):
        # print(file_path)
        #读取文件内容
        with open(file_path, "r", encoding="utf-8") as f:
            #将文件内容添加到列表中
            contents.append(f.read())

print(contents)
#将列表中的内容合并为一个字符串，每个文件内容之间使用换行符\n分隔
final_content = "\n\n".join(contents)
print(final_content)

#将合并后的内容写入到一个新的文件中
with open("D:/python/python练习300题/datas/many_texts/final_texts.txt", "w", encoding="utf-8") as f:
    f.write(final_content)









