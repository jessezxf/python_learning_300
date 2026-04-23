"""
Date:2026/4/5 13:14
Author:Jesse

Python入门习题第16练：输入整数打印星号
需求：提示用户连续输入最多7个整数（每个数在1至50之间，包含1和50）。对于每个有效输入（即在1至50之间的数），程序
将打印该数个数的*。
"""
for i in range(7):

    while True:

        num = int(input('输入一个在1至50之间的数：'))

        if 1 <= num <= 50:
            print('*' * num)
            break
        else:
            print('输入无效，输入一个在1至50之间的数！！\n')
