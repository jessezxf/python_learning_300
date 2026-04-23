"""
Date:2026/4/9 15:04
Author:Jesse

Python入门习题第25练：求前N个数字的平方和
需求：定义一个函数，该函数用于计算从1²到N²的所有整数的平方和。
"""

def sum_of_sequence(n):
    """
    求前N个数字的平方和
    :param n: 前几个数字
    :return: 从1²到N²的所有整数的平方和
    """
    sum = 0
    for i in range(1,n+1):
        # print(i)
        sum = sum + i**2

    return sum

print(sum_of_sequence(5))