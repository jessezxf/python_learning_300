"""
Date:2026/4/16 10:14
Author:Jesse

Python入门习题第33练：计算给定日期是年中的第几天
需求：定义一个函数，该函数接收年份、月份和日期作为参数，计算这一天是该年的第几天。
"""
def is_leap_year(year):
    """
    判断年份是否为闰年
    :param year:
    :return: True  False
    """
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def day_of_year(year,month,day):
    """
    计算给定日期是年中的第几天
    :param year: 年份
    :param month: 月份
    :param day: 日期
    :return: 该日期是该年的第几天
    """
    # 定义一个列表，包含每个月的天数，不考虑闰年的情况
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

    # 判断是否为闰年，如果是闰年，则二月份有29天
    if is_leap_year(year):
        days_in_month[1] = 29  # 修改二月份的天数

    # 计算该日期是年中的第几天
    # 首先计算当前月份之前所有月份的天数总和，然后加上当前月份的天数
    day_count = sum(days_in_month[:month-1]) + day

    # 返回计算结果
    return day_count

year = int(input("输入年份："))
month = int(input("输入月份："))
day = int(input("输入日期："))

print(f"{year}年{month}月{day}日是这一年的第{day_of_year(year,month,day)}天")