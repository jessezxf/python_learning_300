"""
Date:2026/4/22 9:23
Author:Jesse

Python入门习题第64练：日期减法练习
需求：定义一个函数，该函数接收两个参数：一个遵循"YYYY-MM-DD"格式的日期字符串pdate，以及一个整数days。
该函数的任务是计算出从给定日期向前回溯days天后的新日期。
"""
import datetime #导入datetime模块处理日期和时间相关任务


def calculate_previous_date(pdate,days):
    """
    计算并返回给定日期向前回溯days天后的新日期
    :param pdate: 日期字符串，格式为"YYYY-MM-DD"
    :param days: 整数，表示要回溯的天数
    :return: 新日期字符串，格式为"YYYY-MM-DD"
    """
    # 将日期字符串转换为datetime对象
    pdate_obj = datetime.datetime.strptime(pdate,"%Y-%m-%d")
    print(pdate_obj)

    # 创建一个表示days天的时间间隔对象,表示时间差
    time_gap = datetime.timedelta(days=days)
    print(time_gap)


    # 计算新日期,从原日期减去时间差
    pdate_result = pdate_obj - time_gap

    return  pdate_result.strftime("%Y-%m-%d")


print(calculate_previous_date("2026-4-22", 10))



