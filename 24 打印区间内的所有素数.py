"""
Date:2026/4/9 14:48
Author:Jesse

Python入门习题第24练：打印区间内的所有素数
需求：定义一个函数，该函数用于打印指定范围内的所有素数。
素数：一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数。比如3是素数，4不是素数。
"""

def is_prime(number):
    """
    判断一个数是否为素数
    :param number: 要判断的书
    :return: 是，否
    """
    if number <= 1:
        return False

    #遍历2至number-1
    for i in range(2,number):
        if number % i == 0:
            return False

    return True

# print(is_prime(3))


def print_primes(start,end):
    """
    该函数用于打印指定范围内的所有素数
    :param start: 范围起始值
    :param end: 范围结束值
    :return: 无
    """
    for i in range(start,end+1):
        # print(i)
        if is_prime(i) == True:
            print(f'{i}是素数')


print_primes(1,100)