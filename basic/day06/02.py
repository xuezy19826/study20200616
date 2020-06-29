# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          02
# Description:   实现判断一个数是不是回文数    121  倒过来  是  121  所以是回文数
# Author:        xuezy
# Date:          2020/6/29 17:52
# --------------------------------------------------------------


def hws(num):
    """
    判断一个数是否为回文数
    :param num:
    :return:
    """
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + total % 10
        temp //= 10
    return total == num


print('12 是否为回文数：', hws(12))


def hws2(num):
    """
    列表切片，输入的数字转化为字符串 倒叙拼接然后转换为数字 然后判断与输入的内容是否相同
    :param num:
    :return:
    """
    # str() 将内容转换为字符串   list() 将内容转换为列表
    n = list(str(num))
    print(n)
    # 方式一：内容反转，使用切片技术
    #temp = int(''.join(n[::-1]))
    # 方式二：list反转，使用reversed函数
    temp = int(''.join(reversed(n)))
    return num == temp


print('12321 是否为回文数：',hws2(12321))

