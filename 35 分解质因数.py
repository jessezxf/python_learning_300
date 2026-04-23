"""
Date:2026/4/16 11:40
Author:Jesse

Python入门习题第35练：分解质因数
需求：定义一个函数，该函数接收一个正整数n作为参数，并将其分解为质因数，打印出分解的结果。
示例：传入数据90，打印90=2*3*3*5作为质因数分解的结果。
"""
def prime_factorization(n):
    """
    分解质因数
    :param n: 正整数
    :return: 质因数分解结果
    """

    if n == 1:
        print(1)
        return


