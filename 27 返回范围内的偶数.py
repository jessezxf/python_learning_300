"""
Date:2026/4/9 15:33
Author:Jesse

作用：返回指定范围内所有偶数的列表。
参数：start（范围起始值）
end（范围结束值）
返回值：指定范围内所有偶数的列表
"""


def get_even_number(start,end):
    """
    返回指定范围内所有偶数的列表
    :param start: start（范围起始值）
    :param end: end（范围结束值）
    :return: 指定范围内所有偶数的列表
    """
    even_number = []
    for i in range(start,end+1):
        if i % 2 == 0:
            even_number.append(i)

    return even_number


print(get_even_number(1, 10))