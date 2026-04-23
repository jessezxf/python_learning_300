"""
Date:2026/4/20 11:02
Author:Jesse

Python入门习题第43练：整数输入验证
需求：定义一个函数，该函数用于尝试将用户输入的字符串转换为整数。如果转换成功，则返回整数。如果转换失败，则返回错误信！
"""

def string_to_int():
    """
    尝试将用户输入的字符串转换为整数
    :return: 整数（转换成功） 或 错误信息（转换失败）
    """
    try:
        num = int(input("请输入一个整数："))
    except:
        return "输入错误，请输入一个整数！"
    else:
        return num

if __name__ == '__main__':
    print(string_to_int())


