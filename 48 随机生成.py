"""
Date:2026/4/20 14:50
Author:Jesse

Python入门习题第48练：随机生成
需求：编写一个程序，使用random模块来生成各种随机数。
"""

# 导入random模块，用于生成随机数
import random

# random_number = random.random()     # 生成一个[0,1)之间的随机浮点数
# print(random_number)

# random_number2 = random.randint(0,5)    # 生成一个0到5之间的随机整数（包含0和5）
# print(random_number2)


# list1 = [1,2,3,4,5]
# random_number3 = random.choice(list1)   # 从list1中随机选择一个元素
# print(random_number3)


# list1 = [1,2,3,4,5]
list1 = ["a","s","d","f"]
random.shuffle(list1)
print(list1)






