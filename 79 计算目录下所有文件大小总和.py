"""
Date:2026/5/11 18:09
Author:Jesse

D:\python\python练习300题
Python入门习题第79练：计算目录下所有文件大小总和
需求：编写一个程序，计算当前工作目录下所有文件的大小总和，并将结果以千字节（KB）为单位进行打印。
"""
import os

# print(os.path.getsize("Englishpaper.txt"))


#定义变量保存所有文件的大小总和（单位字节）
sum_size = 0

#遍历当前目录下的所有文件和文件夹
for file in os.listdir():
    # print(file)
    #os.path.isfile(文件)：判断路径是否存在且为文件
    if os.path.isfile(file):
        #获取文件大小（单位字节）并累加到总和
        sum_size += os.path.getsize(file)

#打印结果
print(f"当前目录下所有文件大小总和为：{sum_size/1024:.2f}KB")









