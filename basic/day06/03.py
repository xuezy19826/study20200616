# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          03
# Description:   判断一个数是否为素数：大于1的自然数中，除了1和它本身以外不再有其他因数的自然数
# Author:        xuezy
# Date:          2020/6/29 18:18
# --------------------------------------------------------------


def is_prime(num):
    if num <= 1:
        return False
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True


m = int(input('请输入大于1的自然数：'))
print('%d 是否为自然数 ' % m, is_prime(m))