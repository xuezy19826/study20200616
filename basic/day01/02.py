# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          02
# Description:   使用turtle在屏幕上绘制图形,绘制正方形
# Author:        xuezy
# Date:          2020/6/16 16:02
# --------------------------------------------------------------
import turtle
# 设置画笔的宽度
turtle.pensize(14)
# 设置画笔的颜色
turtle.pencolor('red')
# 向当前画笔方向移动distance像素长度   turtle.backward(distance)	向当前画笔相反方向移动distance像素长度
turtle.forward(100)
# 顺时针移动degree°  turtle.left(90)逆时针移动degree°
turtle.right(90)
turtle.forward(100)

turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.mainloop()
