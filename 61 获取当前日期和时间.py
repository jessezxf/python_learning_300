"""
Date:2026/4/21 17:28
Author:Jesse

Python入门习题第61练：获取当前日期时间
需求：编写一个程序，用于获取并显示当前的日期和时间。
"""
import datetime

now_datetime = datetime.datetime.now()
print(now_datetime,type(now_datetime))

#使用strftime()方法将日期时间对象转化为指定格式的字符串输出
print(now_datetime.strftime("%Y-%m-%d %H:%M:%S"))
