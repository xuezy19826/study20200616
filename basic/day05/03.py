# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          03
# Description:   同一个.py文件中的，定义多个同名函数，后面定义的函数会覆盖前面定义的（没有重载的概念）
# Author:        xuezy
# Date:          2020/6/28 16:45
# --------------------------------------------------------------


def foo():
    print('hello,world!')


def foo():
    print('goodbye')


# 输出goodbye
foo()
