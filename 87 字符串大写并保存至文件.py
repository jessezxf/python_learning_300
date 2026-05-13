"""
Date:2026/5/13 10:39
Author:Jesse

Python入门习题第87练：字符串大写并保存至文件
需求：输入一个字符串数据，将其所有小写字母转换为大写字母，并将转换后的字符串保存到磁盘文件test.txt中。
"""
with open("test_87.txt", "w",encoding="utf-8") as f:

    uppercase_string = input("请输入一个字符串：").upper()
    f.write(uppercase_string)

