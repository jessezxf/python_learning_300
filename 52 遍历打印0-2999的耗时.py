"""
Date:2026/4/20 16:01
Author:Jesse

Python入门习题第52练：遍历打印0-2999耗时计算
需求：编写一个程序，该程序将遍历并打印从到2999的所有整数，同时计算并输出整个遍历过程所消耗的总时间。
"""
import time

start_time = time.time()

for i in range(3000):
    print(i)


end_time = time.time()
total_time = end_time - start_time
print("遍历打印0-2999耗时：", total_time, "秒")
