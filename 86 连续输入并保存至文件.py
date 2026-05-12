"""
Date:2026/5/12 17:44
Author:Jesse

Python入门习题第86练：连续输入并保存至文件
需求：编写一个程序，不断提示用户输入数据，直到输入结束符“#”。在输入过程中，将用户每次输入的数据（不包含结
束符"#"）逐行保存到文件中。
"""

#往文件写入内容
with open("input_86.txt","a",encoding="utf-8") as f:
    #死循环持续接收用户输入
    while True:
        #提示用户输入
        input_string = input("请输入内容：")
        #判断用户输入是否为结束符#
        if input_string == "#":
            break
        #将用户输入的内容写入文件
        f.write(input_string+"\n")  #拼接换行符，使每一次输入独占一行











