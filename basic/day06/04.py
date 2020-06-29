# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          04
# Description:   变量作用域问题
# Author:        xuezy
# Date:          2020/6/29 18:29
# --------------------------------------------------------------


def foo():
    b = 'hello'

    # 函数内部可以再定义函数
    def bar():
        c = True

    # NameError: name 'c' is not defined 作用域问题，在当前函数中没有定义C
    print(c)


foo()