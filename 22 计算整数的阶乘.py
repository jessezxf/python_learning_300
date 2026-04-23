"""
Date:2026/4/5 15:20
Author:Jesse

Python入门习题第22练：计算整数的阶乘
需求：定义一个名为factorial的函数，该函数用于计算并返回给定整数的阶乘值。
阶乘：一个正整数的阶乘是所有小于及等于该数的正整数的积，0的阶乘为1。
示例：5的阶乘：1*2*3*4*5；10的阶乘：1*2*3*4*5*6*7*8*9*10。
"""


def factorial(number):
    """
    该函数用于计算整数的阶乘
    :param num: number非负整数
    :return:给定整数的阶乘值
    """
    #负数没有阶乘，判断number是否小于0
    if number<0:
        return print(f'负数没有阶乘')

    #定义变量保存阶乘值
    result = 1

    #遍历1-number
    for i in range(1,number+1):
        # print(i)
        result *= i

    return print(result)

factorial(-5)
factorial(5)
factorial(15)

