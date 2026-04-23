"""
Date:2026/4/4 18:29
Author:Jesse

Python入门习题第14练：输入数字排序
需求：接收用户输入的三个数字，并按从小到大的顺序输出。
"""

#输入3个数据并转换为浮点型
num1 = float(input('输入第一个数据：'))
num2 = float(input('输入第2个数据：'))
num3 = float(input('输入第3个数据：'))

# #方法一
# #比较num1和num2的大小
# if num1 > num2:
#     num1,num2 = num2,num1
#
# #比较num1和num3的大小
# if num1 > num3:
#     num1,num3 = num3,num1
#
# #比较num2和num3的大小
# if num2 > num3:
#     num2,num3 = num3,num2
#
# print('按从小到大的顺序输出为：',num1,num2,num3)



#方式二，使用sorted排序
sorted_numbers = sorted([num1,num2,num3])

print('按从小到大的顺序输出为：',sorted_numbers)