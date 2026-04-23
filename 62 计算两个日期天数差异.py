"""
Date:2026/4/21 17:43
Author:Jesse

Python入门习题第62练：计算两个日期天数差异
需求：编写一个程序，用于计算两个日期之间的天数差异。
"""
import datetime #导入datetime模块处理日期和时间相关任务


birthday = "2000-1-1"


#使用datetime.datetime.strptime（）将出生日期字符串转换为datetime对象
birthday_str = datetime.datetime.strptime(birthday,"%Y-%m-%d")
print(birthday_str,type(birthday_str))

#获取当前时间
current_datetime = datetime.datetime.now()
print(current_datetime,type(current_datetime))

#计算两个日期之间的天数差异
days_diff = current_datetime - birthday_str
print(days_diff,type(days_diff))

#打印天数差
print(f"距离出生日期已经过去了{days_diff.days}天")








