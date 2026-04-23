"""
Date:2026/4/22 10:15
Author:Jesse

Python入门习题第67练：合并字典
需求：定义一个函数，用于将两个给定字典合并。
"""
import copy


def merge_dicts(dict1,dict2):
    """
    将两个给定字典合并
    :param dict1:
    :param dict2:
    :return: 合并后的新字典
    """
    #拷贝dict1，避免修改原始字典
    mergeed_dict1 = copy.copy(dict1)
    print("拷贝dict1:",mergeed_dict1,type(mergeed_dict1))

    #使用update方法将dict2的键值对合并到mergeed_dict1里
    mergeed_dict1.update(dict2)

    return mergeed_dict1




dict1 = {"a":1,"b":5}
dict2 = {"b":2,"c":3,"d":4}

print(merge_dicts(dict1, dict2))

