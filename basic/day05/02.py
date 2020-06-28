# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          02
# Description:   函数的参数：没有指定参数，使用默认值
# Author:        xuezy
# Date:          2020/6/28 16:31
# --------------------------------------------------------------
from random import randint


def roll_dice(n=2):
    """
    摇色子,2为默认值
    :param n:摇色子次数
    :return: 点数之和
    """
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


# 没有指定参数，使用默认值2
print(roll_dice())
# 摇三次色子
print(roll_dice(3))

print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))

# 传递参数时，可以不按照设定的顺序进行传递
print(add(c=1, a=5, b=6))


def add2(*args):
    """
    使用可变参数
    :param args:参数
    :return:
    """
    total = 0
    for n in args:
        total += n
    return total


print('使用可变参数结果：', add2(1, 1, 1, 1, 2))
