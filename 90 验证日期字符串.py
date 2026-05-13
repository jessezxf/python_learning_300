"""
Date:2026/5/13 11:52
Author:Jesse

Python入门习题第90练：验证日期字符串
需求：定义一个函数，用于验证给定的日期字符串是否符合YYYY-MM-DD的格式。
"""
import re   #导入re模块，用于正则表达式相关操作


#定义函数
def check_date(date):
    """
    验证给定的日期字符串是否符合YYYY-MM-DD的格式。
    :param date: 待验证 的日期字符串
    :return: true或false
    """
    #使用正则表达式进行验证
    return re.match(r"\d{4}-\d{2}-\d{2}",date) is not None

#给定日期字符串
date1 ="2025-02-07"
date2 ="202-05-20"
date3 ="2021/05-20"
date4 ="20210520"
date5 ="202a-05-20"

#调用函数进行验证
print(date1,check_date(date1))
print(date2,check_date(date2))
print(date3,check_date(date3))
print(date4,check_date(date4))
