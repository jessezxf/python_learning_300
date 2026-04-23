"""
Date:2026/4/16 16:43
Author:Jesse

Python入门习题第38练：交换列表指定位置元素
需求：定义一个函数，该函数用于将指定列表中指定索引位置的两个元素对调。
示例：给定列表[23，65，19，90]，以及索引位置1和3，调用函数后，打印[23，90，19，65]
"""
li=[10,20,30,40,50]
li2=[23,65,19,90]

def swap_elements(list,pos1,pos2):
    """
    交换列表指定位置元素
    :param list: 列表
    :param pos1: 位置1
    :param pos2: 位置2
    :return:
    """
    if not (0 <= pos1 <= len(list)) or not (0 <= pos2 <= len(list)):
        return "索引位置超出范围"


    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list

print(f"交换前：{li},交换后{swap_elements(li,10,3)}")
print(f"交换前：{li2},交换后{swap_elements(li2,1,3)}")