"""
Date:2026/4/21 17:03
Author:Jesse

Python入门习题第60练：计算指定年月首日星期及天数
需求：编写一个程序，计算并打印出指定年指定月份的第一天是星期几以及该月份的总天数。
"""
import calendar #导入calendar模块处理日历相关任务

year = int(input("请输入年份："))
month = int(input("请输入月份："))

#使用calendar.monthrange（）返回指定年月的第一天是星期几以及该月份的总天数
print(calendar.monthrange(year, month))
first_weekday,num_days = calendar.monthrange(year, month)

weekdays = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]

print(f"{year}年 {month}月的第一天是{weekdays[first_weekday]},该月份共有{num_days}天")
