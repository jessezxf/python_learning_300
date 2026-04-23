"""
Date:2026/4/20 12:23
Author:Jesse

Python入门习题第46练：绘制线条型螺旋图案
需求：请使用Python的tkinter库来创建一个图形界面，并在其中绘制一个由红色线条组成的螺旋形图案。
"""
from tkinter import *       # 导入tkinter库,用于创建图形用户界面


#创建一个Canvas组件，用于绘制图形，并设置宽度和高度均为300像素，背景颜色为白色
canvas = Canvas(width=300,height=300,bg="white")
#使用pack布局管理器将Canvas组件添加到窗口中，并设置其扩展和填充属性以便填满整个窗口
canvas.pack(expand=True,fill=BOTH)


#绘制第一组螺旋形线条
x0,y0 = 163, 163
#初始化第一组线条的终点y坐标偏移量
y1 = 170

#绘制第一组螺旋形线条
for i in range(19):
    # 使用create_line方法绘制直线，其参数分别代表线条的起点坐标和终点坐标
    # 设置线条宽度为1像素，颜色为红色
    canvas.create_line(x0, y0, x0, y1, width=1, fill="red")
    #更新起点坐标，每次向左上方移动5个像素
    x0, y0 = x0 - 5, y0 - 5
    #更新终点y1坐标，每次增加5个像素
    y1 += 5


#绘制第2组螺旋形线条
x0,y0 = 163, 163
#初始化第2组线条的终点y坐标偏移量
y1 = 170

#绘制第一组螺旋形线条
for i in range(19):
    # 使用create_line方法绘制直线，其参数分别代表线条的起点坐标和终点坐标
    # 设置线条宽度为1像素，颜色为红色
    canvas.create_line(x0, y0, x0, y1, width=1, fill="blue")
    #更新起点坐标，每次向左上方移动5个像素
    x0, y0 = x0 + 5, y0 + 5
    #更新终点y1坐标，每次增加5个像素
    y1 += 5


mainloop()



