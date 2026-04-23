"""
Date:2026/4/21 14:36
Author:Jesse

Python入门习题第54练：时间字符串转时间戳
需求：给定一个表示时间的字符串，要求将其转换为以秒为单位的整数时间戳。
"""

import time

# #时间字符串（格式1）
# a1 ="2025-4-10 23:40:00"
#
# # 使用time.strptime() 将时间字符串转换为struct_time对象
# time_array = time.strptime(a1, "%Y-%m-%d %H:%M:%S")
# print(time_array)
#
# # 使用time.mktime() 将struct_time对象转换为时间戳
# timestamp = int(time.mktime(time_array))
# print(timestamp)






#时间字符串（格式2）
a2="2025/4/10 23:40:00"

# # 使用time.strptime() 将时间字符串转换为struct_time对象
# time_array = time.strptime(a2, "%Y/%m/%d %H:%M:%S")
# print(time_array)
#
# # 使用time.mktime() 将struct_time对象转换为时间戳
# timestamp = int(time.mktime(time_array))
# print(timestamp)


#获取当前时间
time2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
print(time2)





