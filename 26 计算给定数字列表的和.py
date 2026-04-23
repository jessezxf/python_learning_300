"""
Date:2026/4/9 15:14
Author:Jesse

Python入门习题第26练：计算列表数字的和
需求：定义一个函数，该函数用于计算并返回给定数字列表中所有数字的总和。
11 1111
#给定数字列表
list1=[1，2，3,4]
list2=[20，4,8，21，15，25]
"""

list1=[1,2,3,4]
list2=[20,4,8,21,15,25]


def sum_of_list(number_list):
    """
    计算列表数字的和
    :param number_list: 给定的列表
    :return: 给定数字列表中所有数字的总和
    """
    sum = 0
    for i in number_list:
        sum = sum + i

    return sum

#调用求和函数
print(f'列表list1的和为：{sum_of_list(list1)}')
print(f'列表list2的和为：{sum_of_list(list2)}')

#用内置函数求和，sum（序列)：对序列进行求和计算
print(f'列表list1的和为：{sum(list1)}')
print(f'列表list2的和为：{sum(list2)}')

