# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          05
# Description:   定义一个类描述平面上的点并提供移动点和计算到另一个点的距离
#                公式：两点的坐标是(x1,y1)和(x2,y2)  则两点之间的距离公式为 d=√[(x1-x2)²+(y1-y2)²]
# Author:        xuezy
# Date:          2020/7/8 16:11
# --------------------------------------------------------------
from math import sqrt


class Point(object):

    def __init__(self, x=0, y=0):
        """
        初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """
        移动到指定位置
        :param x: 新的横坐标
        :param y: 新的纵坐标
        :return:
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """
        移动指定增量
        :param dx: 横坐标增量
        :param dy: 纵坐标增量
        :return:
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """
        计算与另一个点的距离
        :param other: 另一个点
        :return:
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == '__main__':
    main()
