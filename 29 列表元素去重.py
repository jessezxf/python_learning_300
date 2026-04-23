"""
Date:2026/4/9 15:47
Author:Jesse

Python入门习题第29练：列表元素去重
需求：定义一个函数，该函数用于对列表进行去重处理，并返回一个新的列表，其中不包含任何重复的元素。
示例：原始列表：[10，20，30，10，20]，去重后：[10，20，30]
"""


list1 = [10,20,30,10,20]

def remove_duplicates(list1):
    """
    列表元素去重
    :param list1: 原始列表
    :return: =去重后的列表
    """
    # #定义不重复的列表
    # result = []
    #
    # #遍历list1
    # for i in list1:
    #     if i not in result:
    #         result.append(i)
    #
    # return result


    #快速去重，转换成集合set再转换回列表
    return list(set(list1))

print(f'从{list1}中去重后的结果为{remove_duplicates(list1)}')