"""
Date:2026/4/16 11:18
Author:Jesse

Python入门习题第34练：
需求：定义一个函数，该函数用于计算斐波那契数列中的第n项。
斐波那契数列：数列的前两项均为1，从第三项开始，每一项都是其前两项的和。如：1、1、2、3、5、8、13、21、34、···
"""
def fibonacci(n):

    """
    计算斐波那契数列的第n项
    斐波那契数列定义：F(1) = 1, F(2) = 1, F(n) = F(n-1) + F(n-2) (n≥3)

    参数:
        n (int): 要计算的斐波那契数列的项数

    返回:
        int: 第n项的斐波那契数
    """
    if n <= 0:
        return "输入的数字必须大于0"


    elif n == 1 or n == 2:  # 基本情况：第1项和第2项都是1
        return 1
    else:  # 递归情况：当前项等于前两项之和
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("请输入要计算的斐波那契数列的第n项："))
print(fibonacci(n))

