# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          04
# Description:   打印三角形
# Author:        xuezy
# Date:          2020/6/19 19:05
# --------------------------------------------------------------

param = '*'
for i in range(1, 6):
    print(param)
    param += '*'

print()

param1 = '*'
nul = ' '
for j in range(5, 0, -1):
    j -= 1
    print(j * nul, (5 - j) * param1)

print()

param2 = '*'
nul2 = ' '
le = 9
for k in range(1, 10, 2):
    tempNul = int((le - k) / 2)
    print(tempNul * nul2, k * param2, tempNul * nul2)