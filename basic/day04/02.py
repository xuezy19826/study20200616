# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          02
# Description:   寻找“完美数”
#                   完美数是除自身外其他所有因子的和正好等于这个数本身的数
#                   例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
# Author:        xuezy
# Date:          2020/6/24 14:43
# --------------------------------------------------------------
import math

wmsList = []

for num in range(1, 10000):
    """
    根据输入的数字判断是否为完美数
    :param num:数字
    :return:
    """
    sums = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            sums += factor
            if factor > 1 and factor != num // factor:
                sums += num // factor

    if sums == num and sums != 1:
        wmsList.append(num)

print('1~10000之间的完美数为：', wmsList)