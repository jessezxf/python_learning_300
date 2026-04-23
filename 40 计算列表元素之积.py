"""
Date:2026/4/16 17:12
Author:Jesse

Python入门习题第40练：计算列表元素之积
需求：定义一个函数，该函数接收一个整数列表作为参数，并返回列表中所有元素的乘积。
示例：给定列表[1，2，3]，调用函数后，返回6（即计算1*2*3）
"""
li=[1,2,3,4]
li2=[8,3,5,7,9]

def product_of_list(lst):
    """
    计算列表元素之积
    :param lst:
    :return: 返回列表中所有元素的乘积
    """
    result=1

    for i in lst:
        # print(i)
        result *= i
    return result

print(product_of_list(li))
print(product_of_list(li2))



