"""
Date:2026/4/21 16:56
Author:Jesse

Python入门习题第59练：打印指定年月日历
需求：编写一个程序，要求用户输入年份和月份，打印出该月份对应的日历。
"""

import calendar # 导入日历模块

year = int(input("请输入年份："))
month = int(input("请输入月份："))

#使用calendar.month()，打印指定年月日历
print(calendar.month(year,month))
