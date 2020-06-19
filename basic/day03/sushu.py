# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          sushu
# Description:   判断输入的数字是否为素数（质数）  大于1的自然数 并且 只能被1和本身整除
# Author:        xuezy
# Date:          2020/6/19 18:37
# --------------------------------------------------------------
from math import sqrt

num = int(input("请输入正整数："))
end = int(sqrt(num))
is_Prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_Prime = False
        break
if is_Prime and num != 1:
    print('%d 是素数' % num)
else:
    print('%d 不是素数' % num)
