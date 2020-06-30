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
    # print(c)

foo()


def foo2():
    # 定义全局变量   和 在函数外面声明的变量 一样
    global a
    a = 200
    print(a)


def foo3():
    print(a)


c = 1


def outer():
    c = 2

    def inner():
        # 当使用nonlocal声明变量 a 时，就会往上最近一层局部作用域寻找局部变量 a ，不能是全局变量（在函数中用global修饰）,也不能在最外层（全局变量）
        nonlocal c
        c = 3

        def inner2():
            print(c)
        inner2()
        print(c)
    inner()
    print(c)


# outer()
# print(c)

if __name__ == '__main__':
#     a = 100
#     print(a)
#     foo2()
#     print(a)
#     print('foo3()', foo3())
#     print('outer()', outer())
    outer()
    print(c)
