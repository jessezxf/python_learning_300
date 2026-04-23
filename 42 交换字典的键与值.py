"""
Date:2026/4/20 10:51
Author:Jesse

Python入门习题第42练：交换字典键与值
需求：定义一个函数，用于交换指定字典的key和value。
示例：给定字典{'a'：1，'b'：2，'c'：3}，调用函数后，返回{1:'a'，2：'b'，3:'c'}
"""
# 给定字典
original_dict ={'a':1, 'b':2, 'c':3}

def swap_dict_keys_values(dct):
    """
    交换字典键与值
    :param dct: 要交换的字典
    :return: 交换后的新字典
    """
    #定义新字典保存交换后的键值对
    swapped_dict = {}

    #遍历原字典的键
    for key in dct:
        # print(key)
        # print(dct[key])
        swapped_dict[dct[key]] = key

    return swapped_dict

print(f"原始字典：{original_dict}")
print(swap_dict_keys_values(original_dict))
