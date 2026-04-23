"""
Date:2026/4/4 18:09
Author:Jesse

Python入门习题第13练：按序插入列表
需求：给定一个已排序的整数列表，要求输入一个数，并根据列表原有的排序规律将其插入到正确的位置上。
#定义一个己排序的整数列表
li=[21，33，57，88，95]
"""

li = [21,33,57,88,95]

#用户输入数据并将其转换为整形
num = int(input('请输入一个数：'))

for i in range(len(li)):
    if li[i] > num:
        #在位置i扎入num
        li.insert(i,num)
        #退出循环
        break
#如果循环正常结束（没有通过break跳出，即未找到插入点），说明num应该放在列表末尾==>循环中的else语句
else:
    li.append(num)

print(li)
