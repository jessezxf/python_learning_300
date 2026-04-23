"""
Date:2026/4/9 16:03
Author:Jesse

Python入门习题第30练：变量互换
需求：定义一个函数，该函数用于实现两个变量值的互换操作。
"""

def swap_values(var1,var2):
    """
    该函数用于实现两个变量值的互换操作
    :param var1:
    :param var2:
    :return:
    """
    return var2,var1

name1 = "feifei"
name2 = 'susu'

name1, name2 = swap_values(name1, name2)
print(name1)
print(name2)
