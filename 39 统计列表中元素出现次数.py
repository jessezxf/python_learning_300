"""
Date:2026/4/16 16:57
Author:Jesse

Python入门习题第39练：统计列表中元素出现次数
需求：定义一个函数，该函数用于统计指定元素在指定列表中出现的次数。
"""

li=[1,2,3,4,2,2,5,2,6]



def count_num(lst,element):
    """
    统计列表中元素出现次数
    :param li:
    :param num:
    :return:指定元素出现的次数
    """
    count = 0
    for i in lst:
        # print(i)
        if i == element:
            count += 1

    return count


print(f"列表{li}中，元素2出现了{count_num(li, 2)}次")
print(f"列表{li}中，元素7出现了{count_num(li, 7)}次")


#内置函数  列表.count(元素)
print(li.count(2))
print(li.count(7))

