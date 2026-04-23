"""
Date:2026/4/20 11:26
Author:Jesse

Python入门习题第45练：绘制螺旋形圆圈图案
需求：请使用Python的tkinter库来创建一个图形界面，并在其中绘制一个由圆圈组成的螺旋形图案。
"""

from tkinter import *       # 导入tkinter库,用于创建图形用户界面

#创建一个Canvas组件，用于绘制图形，并设置宽度500像素，高为
canvas = Canvas(width=500,height=400)

# 将Canvas组件添加到窗口中，并设置扩展和填充属性以便填满整个窗口
canvas.pack(expand=True,fill=BOTH)

#初始化k，用于控制圆圈的半径
k = 1
#初始化变量j，用于控制每次循环中K的增量，从而控制圆圈之间的大小差异
j = 1

#绘制26个圆圈，形成螺旋图案
for i in range(26):
    #使用create_oval方法绘制圆圈，其参数反别代表圆圈的左上角和右下角坐标
    canvas.create_oval(250-k,200-k,250+k,200+k,width=1)

    #每次循环结束后，k和j的值都增加1，从而使得下一个圆圈的半径和大小都增加
    # j控制K的增量，从而控制圆圈增长的速度
    k += j
    # 同时，每次循环后也增加j的值，这样圆圈之间的增长差异会逐渐变大，形成螺旋形的效果
    j += 0.5

#进入tkinter的主事件循环，这样窗口就会保持打开状态并响应用户的操作（如关闭窗口）
mainloop()
