"""
Date:2026/4/5 14:39
Author:Jesse

Python入门习题第21练：计算连续数字串和
需求：编写一个程序，计算a+aa+aaa+aaaa+··.的值，其中a是一个数字，且加数的个数由键盘输入决定。例如，当a=2
且共有5个数相加时，表达式为2+22+222+2222+22222。
"""

n = int(input('输入加数的个数：'))
a = int(input('输入数字：'))

for i in range(1,n+1):
    print(i)

