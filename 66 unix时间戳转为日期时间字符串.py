"""
Date:2026/4/22 10:04
Author:Jesse

Python入门习题第66练：Unix时间戳转日期时间字符串
需求：编写一个程序，给定一个Unix时间戳（例如：1620747224），
请将其转换为对应的日期和时间字符串，格式为"YYYY-MM-DDHH：MM：SS"。
"""
import datetime

unix_time = 1720747224


#使用datetime.datetime.fromtimestamp（）将unix时间戳转换为datetime对象
date_object = datetime.datetime.fromtimestamp(unix_time)
print(date_object,type(date_object))


#ji将datetime对象转换为指定格式的日期时间字符串
date_object = datetime.datetime.fromtimestamp(unix_time).strftime('%Y/%m/%d %H:%M:%S')
print(date_object,type(date_object))










