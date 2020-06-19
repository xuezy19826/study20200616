# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          02
# Description:   使用turtle在屏幕上绘制图形,绘制太阳花
# Author:        xuezy
# Date:          2020/6/16 16:15
# --------------------------------------------------------------
import turtle as t
import time
t.color("red", "yellow")
# 速度 0~10
t.speed(2)
t.begin_fill()
for _ in range(50):
    t.forward(200)
    t.left(170)
t.end_fill()
time.sleep(1)
