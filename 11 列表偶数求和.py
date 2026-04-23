"""
Date:2026/4/4 17:45
Author:Jesse

Python入门习题第11练：列表偶数求和
需求：给定一个整数列表，计算并打印该列表中所有偶数的和。
11 1111
#定义一个整数列表
numbers=[1,2,3,4,5,6,7,8,9,10]
"""

numbers=[1,2,3,4,5,6,7,8,9,10]
#定义变量总和
result = 0

#遍历列表
for number in numbers:
    #判断是否位偶数
    if number % 2 == 0:
        print(number)
        result += number
print("列表中所有偶数的和位：",result)

