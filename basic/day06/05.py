# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          05
# Description:   闭包和匿名函数
# Author:        xuezy
# Date:          2020/6/30 11:08
# --------------------------------------------------------------


def FunX(x):
    """
    闭包：一个闭包就是你调用了一个函数A，这个函数A返回了一个函数B给你。这个返回的函数B就叫做闭包。
    :param x:
    :return:
    """
    def FunY(y):
        return x * y
    return FunY


tempx = FunX(3)
result = tempx(5)
print('调用闭包函数结果为：%d' % result)


# 匿名函数
# lambda函数的语法只包含一个语句： lambda [arg1 [,arg2,.....argn]]:expression
# 冒号左边→想要传递的参数
# 冒号右边→想要得到的数（可能带表达式）
square = lambda x: x ** 3
print('调用匿名函数square结果为：%d' % square(3))

sum = lambda x, y : x + y
print('调用匿名函数sum结果为：%d' % sum(2, 3))
