"""
Date:2026/4/9 16:11
Author:Jesse

Python入门习题第31练：计算字典值总和
需求：定义一个函数，该函数接收一个字典作为参数，并返回该字典中所有值的总和。
example_dict ={"a":100, "b":200, "c":300}
"""

example_dict ={"a":100, "b":200, "c":300, "d":400}

def sum_dict_value(dict1):
    """
    计算字典值总和
    :param dict1: 需要计算值总和的字典
    :return: 返回字典中所有值的总和
    """
    result = 0  # 初始化结果变量为0
    for i in dict1.values():  # 遍历字典中的所有值
        result += i  # 将每个值累加到结果中

    return result  # 返回计算得到的结果


print(f'{example_dict}中值的总和为',sum_dict_value(example_dict))