"""
Date:2026/4/5 13:42
Author:Jesse

Python入门习题第19练：进制转换
需求：用户输入一个数字，实现十进制向二进制、八进制、十六进制的转换功能，并打印出转换结果。
"""

# num = int(input('输入数字：'))
#
# #用内置函数实现转换
# print('十进制数为：',num)
# print('转换为二进制数为：',bin(num))
# print('转换为8进制数为：',oct(num))
# print('转换为16进制数为：',hex(num))

def conversion_number(num):
    """

    :param num: 输入的十进制数
    :return: 打印输出
    """
    print('十进制数为：', num)
    print('转换为二进制数为：', bin(num))
    print('转换为8进制数为：', oct(num))
    print('转换为16进制数为：', hex(num))

conversion_number(13)