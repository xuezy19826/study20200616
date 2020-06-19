# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          05
# Description:   if练习
# Author:        xuezy
# Date:          2020/6/18 19:20
# --------------------------------------------------------------
import math

"""
练习1：英制单位与公制单位互换
"""
value = float(input("请输入长度："))
unit = input("请输入单位：")
if unit == 'in' or unit == '英寸':
    print('%.3f英寸 = %.3f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%.3f厘米 = %.3f英寸' % (value, value / 2.54))
else:
    print('请输入有效单位')


"""
练习2：投骰子
"""
from random import randint
face = randint(1, 6)
if face == 1:
    print('1 吃苹果')
elif face == 2:
    print('2 吃香蕉')
elif face == 3:
    print('3 吃栗子')
elif face == 4:
    print('4 吃柿子')
elif face == 5:
    print('5 喝水')
else:
    print('6 休息')

"""
练习3：输入三条边长，如果能构成三角形，则计算周长和面积
"""
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长： %.0f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积：%.2f' % area)
else:
    print('不能构成三角形')

