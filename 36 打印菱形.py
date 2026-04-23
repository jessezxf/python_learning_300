"""
Date:2026/4/16 11:49
Author:Jesse

Python入门习题第36练：打印菱形
需求：定义一个函数，该函数接收一个正整数参数rows，其功能是打印出一个由星号*构成的、具有rows指定行数的菱形图案。
"""
def print_rhombus(rows):
    """
    打印一个由星号*构成的菱形图案
    参数：rows 菱形的总行数，必须为奇数
    :return: 无
    """

    if rows % 2 == 0:
        print("行数必须是奇数")
        return #结束运行

    #打印上半部分（不包含中建行）
    for i in range(1, rows, 2):
        #前导空格
        space = " " * ((rows - i) // 2)
        #星号
        star = "*" * i
        #打印当前行
        print(space + star)

    #打印下半部分（包含中建行）
    for i in range(rows, 0, -2):
        # 前导空格
        space = " " * ((rows - i) // 2)
        # 星号
        star = "*" * i
        # 打印当前行
        print(space + star)



print_rhombus(7)
print_rhombus(4)
print_rhombus(9)

