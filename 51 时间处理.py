"""
Date:2026/4/20 15:31
Author:Jesse

Python入门习题第51练：时间处理
需求：编写一个程序，使用time模块来实现时间处理功能。
"""
import time

# current_time = time.time() # 获取当前时间戳,即自纪元（1970-01-0100:00:00）以来的秒数
# print(current_time)  # 1776670425.4775183



# time.ctime()  # 获取当前时间，格式为：'Mon Oct  7 22:43:26 2019'
# current_time_str = time.ctime()
# print(current_time_str)  #Mon Apr 20 15:37:43 2026

# specified_time_str = time.ctime(1779690426) #将指定时间戳转换为时间字符串
# print(specified_time_str)



# time.localtime()  # 将时间戳转换为本地时间的struct_time对象（年、月、日、时、分、秒等）。没有指定参数，则默认使用当前时间
# current_local_time = time.localtime()
# print(current_local_time)

# specified_local_time = time.localtime(1776670425) #获取指定时间戳的struct_time对象
# print(specified_local_time)



# time.gmtime()   # 将时间戳转换为UTC时间的struct_time对象（年、月、日、时、分、秒等）。没有指定参数，则默认使用当前时间
# current_utc_time = time.gmtime() #获取当前时间戳的struct_time对象（UTC时间）
# print(current_utc_time)

# specified_utc_time = time.gmtime(1776670425)    #获取指定时间戳的struct_time对象（UTC时间）
# print(specified_utc_time)



#time.asctime()：将struct_time对象转换为特定格式的字符串表示（格式为：星期 月份 日 时：分：秒 年）
local_time = time.asctime(time.localtime())
print(local_time) #Mon Apr 20 15:43:26 2026












