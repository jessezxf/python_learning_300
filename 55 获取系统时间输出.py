"""
Date:2026/4/21 15:32
Author:Jesse

Python入门习题第55练：延时操作
需求：编写一个程序，该程序在暂停一秒后获取当前系统时间，并将其转换为"YYYY-MM-DDHH：MM：SS"格式的字符串进行打印。
"""
import time

time1 = time.strftime("%Y-%m-%d-%A, %H:%M:%S", time.localtime())
print(time1)

time.sleep(1)

time2 = time.strftime("%Y-%m-%d-%A, %H:%M:%S", time.localtime())
print(time2)