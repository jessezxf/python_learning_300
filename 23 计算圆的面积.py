"""
Date:2026/4/9 14:36
Author:Jesse

Python入门习题第23练：计算圆的面积
需求：定义一个函数，该函数用于计算并返回给定半径的圆的面积（要求结果保留两位小数）。
1111
"""
import math
print(math.pi)
def area_of_circle(r):
    """
    该函数用于计算并返回给定半径的圆的面积（要求结果保留两位小数）
    :param r: 圆的半径
    :return: 圆的面积，结果保留两位小数
    """
    area = math.pi * r * r

    #保留两位小数：round(浮点数，小数点后要保留的位数)
    area = round(math.pi * r * r,2)

    return area

#调用函数并接收返回值
print('半径为2的圆的面积为：',area_of_circle(2))

