"""
Date:2026/4/20 14:39
Author:Jesse

Python入门习题第47练：绘制矩形螺旋图案
需求：请使用Python的tkinter库来创建一个图形界面，并在其中绘制一个由矩形组成的螺旋形图案。
"""
from tkinter import *       # 导入tkinter库,用于创建图形用户界面


#创建一个Canvas组件，用于绘制图形，并设置宽度和高度均为300像素，背景颜色为白色
canvas = Canvas(width=300,height=300,bg="white")
#使用pack布局管理器将Canvas组件添加到窗口中，并设置其扩展和填充属性以便填满整个窗口
canvas.pack(expand=True,fill=BOTH)


#初始化第一个矩形的左上角坐标
x0,y0 = 140,140
#初始化第一个矩形的右下角坐标
x1,y1 = 160,160

#绘制19个矩形，形成螺旋形图案
for i in range(19):
    #使用create_rectangle方法创建一个矩形，参数为左上角和右下角的坐标
    canvas.create_rectangle(x0,y0,x1,y1)
    #更新下一个矩形的左上角和右下角坐标
    x0 -= 5
    y0 -= 5
    x1 += 5
    y1 += 5


#运行tkinter主循环，以便窗口保持打开状态，直到用户关闭窗口
mainloop()


