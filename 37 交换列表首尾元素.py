"""
Date:2026/4/16 12:10
Author:Jesse

Python入门习题第37练：交换列表首尾元素
需求：定义一个函数，该函数接收一个列表newList作为参数。函数的功能是交换该列表的第一个元素和最后一个元素，并返回交换后的
列表。
示例：给定列表newList=[1，2，3]，调用函数后，应打印出[3，2，1]
"""
# 给定列表
li=[1,2,3]
li2=['a', 'b', 'c', 'd', 'e']
li3=[]
li4=[1]

def swap_first_last(newList):
    """
    交换列表首尾元素
    :param newList:要交换元素的列表
    :return: 交换后的列表
    """
    # 判断列表是否为空,或只有一个元素
    if len(newList) <= 0:
        return newList

    # 交换首尾元素，利用python的元组解包
    newList[0], newList[-1] = newList[-1], newList[0]
    return newList



print(f"交换前：{li},交换首尾元素后：{swap_first_last(li)}")
print(f"交换前：{li2},交换首尾元素后：{swap_first_last(li2)}")
print(f"交换前：{li3},交换首尾元素后：{swap_first_last(li3)}")
print(f"交换前：{li4},交换首尾元素后：{swap_first_last(li4)}")

