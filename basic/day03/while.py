# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          while
# Description:   while循环
# Author:        xuezy
# Date:          2020/6/19 17:27
# --------------------------------------------------------------
import random

"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
分别提示：大一点/小一点/猜对了
"""
answer = random.randint(1, 100)
count = 0
while True:
    count += 1
    number = int(input("请输入数字："))
    if number > answer:
        print("大一点")
    elif number < answer:
        print("小一点")
    else:
        print("猜对了")
        break
print('总共猜了%d次' % count)
if count > 5:
    print('猜的次数太多了')

