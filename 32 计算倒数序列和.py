"""
Date:2026/4/9 17:51
Author:Jesse

Python入门习题第32练：计算倒数序列和
需求：定义一个函数，该函数用于根据传入的整数n返回对应的倒数序列和：若n为偶数，则计算和1/2+1/4+···+1/n；若n
为奇数，则计算和1/1+1/3+·..+1/n。
"""

def sum_daoshu(n):
    """
    计算倒数序列和
    :return: 对应倒数序列和
    """
    result = 0

    if n <= 0:
        return "None,输入必须为正整数"

    if n % 2 == 0:
        for i in range(2,n+1,2):
            # print(1/i)
            result += 1/i
    else:
        for i in range(1,n+1,2):
            # print(1/i)
            result += 1 / i

    return result
print(sum_daoshu(3))
print(sum_daoshu(5))
print(sum_daoshu(-3))
