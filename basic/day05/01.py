# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          01
# Description:   阶乘
# Author:        xuezy
# Date:          2020/6/28 16:23
# --------------------------------------------------------------


def factorial(num):
    """
    求阶乘
    :param num:非负整数
    :return: num的阶乘
    """
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


m = int(input("m = "))
print('m的阶乘为%d' % factorial(m))
