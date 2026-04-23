"""
Date:2026/4/21 15:51
Author:Jesse

Python入门习题第56练：实现简单秒表
需求：编写一个程序，实现简单秒表功能。该程序在用户按下回车键后开始计时，在用户中断程序时停止计时。
"""
import time

print("按下回车键后开始计时,中断程序停止计时~~~~~~~~~")
input("准备...")

start_time = time.time()

print("计时中...")

try:
    while True:
        total_time = time.time() - start_time

        # \r表示每一个输出都覆盖同行的第一位，end=""表示不换行
        print(f"\r计时：{total_time:.0f}秒", end="")

        time.sleep(1)
except KeyboardInterrupt:
    # KeyboardInterrupt是用户中断程序时触发的异常,捕获用户中断程序的信号

    total_time = time.time() - start_time
    print(f"\n计时结束,总时间为：{total_time:.0f}秒")


