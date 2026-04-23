"""
Date:2026/4/22 8:49
Author:Jesse

Python入门习题第63练：简单日期处理
需求：编写一个程序，使用datetime模块完成以下任务：
1.输出今日日期（YYYY-MM-DD格式）。
2.创建并输出明日香生日（1941年1月5日）的日期。
3.计算并输出明日香生日的下一天。
4.计算并输出明日香的一岁生日日期。
"""
import datetime #导入datetime模块处理日期和时间相关任务

print(datetime.datetime.now().strftime("%Y/%m/%d")) #输出今日日期（YYYY-MM-DD格式）



#创建并输出明日香生日（1941年1月5日）的日期
birthday = datetime.date(1941,1,5)
print("明日香生日：",birthday)

#计算并输出明日香生日的下一天
birth_next_day = birthday + datetime.timedelta(days=1)
print("明日香生日的下一天：",birth_next_day)








