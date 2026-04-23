"""
Date:2026/4/22 9:43
Author:Jesse

Python入门习题第65练：生成日期范围列表
需求：定义一个函数，它接收两个遵循"YYYY-MM-DD"格式的日期字符串参数begin_date和end_date。
该函数的任务是生成一个包含从begin_date到end_date（包括两端日期在内）所有日期的列表，并将该列表作为结果返回。
"""
import datetime


def get_date_range(begin_date,end_date):
    """
    生成一个包含从begin_date到end_date（包括两端日期在内）所有日期的列表，并将该列表作为结果返回。
    :param begin_date:起始日期
    :param end_date:结束日期
    :return:（包括两端日期在内）所有日期的列表
    """

    #将日期字符串转换为datetime对象
    begin_date_obj = datetime.datetime.strptime(begin_date,"%Y-%m-%d")
    end_date_obj = datetime.datetime.strptime(end_date,"%Y-%m-%d")

    #创建一个空列表，用于存储日期
    date_list = []

    #定义变量保存日期对象，初始值为当前日期
    current_date = begin_date_obj

    #使用while循环生成日期列表
    while current_date <= end_date_obj:
        #将日期对象转换为字符串，并添加到列表中
        date_list.append(current_date.strftime("%Y-%m-%d"))
        #将当前日期对象增加一天
        current_date += datetime.timedelta(days=1)

    return date_list


print(get_date_range("2022-01-01", "2022-01-10"))







