# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          07
# Description:   双色球选号
# Author:        xuezy
# Date:          2020/7/7 18:27
# --------------------------------------------------------------
from random import randrange,randint,sample


def display(balls):
    """
    输出列表中的双色球号码
    :param balls:
    :return:
    """
    # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，如：
    # >>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    # >>> list(enumerate(seasons))
    # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        # %02d  两位数字 不够左边补0
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    :return:
    """
    red_balls = [x for x in range(1, 34)]
    select_balls = []
    # 从列表中随机抽取6个元素
    select_balls = sample(red_balls, 6)
    select_balls.sort()
    select_balls.append(randint(1, 16))
    return select_balls


def main():
    n = int(input('机选几注：'))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()


