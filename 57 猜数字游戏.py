"""
Date:2026/4/21 16:20
Author:Jesse

需求：编写一个程序，实现数字猜谜游戏并测试反应速度。
该程序会生成一个0至99间的随机数字供用户猜测，通过实时反馈引导用户直至猜中。
同时，程序会记录用户的猜测耗时，并在游戏结束时提供表现反馈。
"""

import random,time

#生成一个0-99之间的随机整数
target_munber = random.randint(0,99)

#保存游戏开始时间
start_time = time.time()

print(f"欢迎来到猜数字游戏！{target_munber}")
print("我已经想好了一个0-99之间的数字，你能猜到它是几吗？？？？？？？")


while True:
    try:
        #获取用户输入并转换为整形
        guess = int(input("输入你的猜测："))
    except ValueError:
        print("请输入一个有效的数字！")
    else:
        #判断猜测数字与目标数字的大小关系
        if guess < target_munber:
            print("猜小了！")
        elif guess > target_munber:
            print("猜大了！")
        else:
            # print("恭喜你，猜对了！")
            #保存猜中时间
            end_time = time.time()
            #退出循环
            break

#计算总耗时
total_time = end_time - start_time
# print(f"你用了{total_time:.2f}秒猜中了数字{target_munber}！")


#提供表现反馈
if total_time < 5:
    print(f"恭喜你猜中了！！！！你的反应时间非常快，只用了{total_time:.2f}秒")
elif total_time < 10:
    print(f"猜中了！你的反应时间快，用了{total_time:.2f}秒")
else:
    print(f"终于猜中了！你的反应时间用了{total_time:.2f}秒")









