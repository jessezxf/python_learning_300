"""
Date:2026/4/5 13:56
Author:Jesse

Python入门习题第20练：平方运算
持续提示用户输入一个数字，并对该数字进行平方运算。如果平方运算结果小于50，则停止输入。
"""
while True:

    num = int(input('输入一个数字：'))

    result = num ** 2
    print(f'数字{num}的平方是{result}')
    if result < 50:
        break
