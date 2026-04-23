"""
Date:2026/4/16 17:22
Author:Jesse

Python入门习题第41练：翻转头尾并拼接字符串
需求：定义一个函数，该函数接收一个字符串和一个整数作为参数。完成以下操作：
1.从字符串头部截取指定数量的字符并翻转。
2.从字符串尾部截取相同数量的字符并翻转。
3.分别打印出头部和尾部翻转后与剩余部分拼接后的新字符串。
"""

def rotate_and_concat(s,d):
    """
    从字符串头部和尾部截取指定数量的字符并翻转，与剩余部分拼接并打印
    :param s:
    :param d:
    :return:
    """

    if d > len(s):
        print("指定的字符数量超过了字符串的长度")
        return

    #从字符串头部截取指定数量的字符串并反转
    head_flipped = s[:d][::-1]
    #头部剩余部分
    head_rest = s[d:]
    #头部反转后与剩余部分拼接
    head_result = head_flipped + head_rest

    # 从字符串尾部截取指定数量的字符串并反转
    tail_flipped = s[-d:][::-1]
    # 尾部剩余部分
    tail_rest = s[:-d]
    # 尾部反转后与剩余部分拼接
    tail_result = tail_rest + tail_flipped

    print(f"头部翻转后与剩余部分拼接后的新字符串为：{head_result}")
    print(f"尾部翻转后与剩余部分拼接后的新字符串为：{tail_result}")

input_string = "abcdefghi"
num_chars = 2

rotate_and_concat(input_string, num_chars)