"""
Date:2026/4/9 15:38
Author:Jesse

Python入门习题第28练：移除列表中的多个元素
需求：定义一个函数，该函数用于从第一个列表飞ist1中移除所有存在于第二个列表飞ist2中的元素。
示例：原始列表：[3，5，7，9，11，13]，移除元素列表：[7，11]，移除后：[3，5，9，13]
# 给定列表
list1=[3,5,7,9,11,13]
list2=[7，111]
"""
list1=[3,5,7,9,11,13]
list2=[7,11]


def remove_element(list1,list2):
    """
    从第一个列表飞ist1中移除所有存在于第二个列表list2中的元素
    :param list1:原始列表
    :param list2:要移除元素的列表
    :return:移除指定元素后的列表
    """
    #遍历list1
    for i in list2:
        if i in list1:
            list1.remove(i)

    return list1

print(f'从{list1}中移除{list2}后的列表为{remove_element(list1,list2)}')