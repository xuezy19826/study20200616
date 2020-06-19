# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          03
# Description:   test
# Author:        xuezy
# Date:          2020/6/18 18:44
# --------------------------------------------------------------
import math

"""
练习1：将华氏温度转为摄氏温度
公式：F = 1.8C + 32
"""
f = float(input("请输入华氏温度："))
c = (f - 32)/1.8

# %.1f 表示传参  保存一位小数
print('%.1f华氏度 = %.1f摄氏度' % (f, c))


"""
练习2：输入圆的半径，计算周长和面积
"""
radius = float(input("请输入圆的半径："))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长：%.2f' % perimeter)
print('面积：%.2f' % area)


"""
练习3：输入年份判断是不是闰年
"""
year = int(input("请输入年份："))
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print(is_leap)

