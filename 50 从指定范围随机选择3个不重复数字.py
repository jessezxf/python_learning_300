"""
Date:2026/4/20 15:21
Author:Jesse

Python入门习题第50练：从指定范围随机选择3个不重复数字
需求：编写一个程序，该程序能够从用户指定的数字范围中随机选择3个不重复的数字。
"""
import random

start = int(input("输入开始范围数字："))
stop = int(input("输入结束范围数字："))

#random.sample（population，k)：从指定的序列population中随机选择k个不重复的元素
random_sample = random.sample(range(start, stop+1), 3)

print(random_sample)

