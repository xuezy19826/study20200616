# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          02
# Description:   静态方法（使用注解@staticmethod）
#                传入三条边长 来构造三角形，并计算周长和面积
# Author:        xuezy
# Date:          2020/7/8 17:08
# --------------------------------------------------------------
from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        """
        初始化方法
        :param a: 边长
        :param b: 边长
        :param c: 边长
        """
        self._a = a
        self._b = b
        self._c = c

    # 该注解表示当前方法为 静态方法
    @staticmethod
    def is_valid(a, b, c):
        """
        判断是否构成三角形
        :param a: 边长
        :param b: 边长
        :param c: 边长
        :return: 可以构成三角形 返回True  否则返回False
        """
        return a + b > c and a + c > b and b + c > a

    def permiter(self):
        """ 计算三角形周长 """
        return self._a + self._b + self._c

    def area(self):
        """ 计算三角形面积 """
        helf = self.permiter() / 2
        return sqrt(helf * (helf - self._a) * (helf - self._b) * (helf - self._c))


def main():
    a, b, c = 3, 4, 5
    print('三条边长分别为：%d,%d,%d' % (a, b, c))
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print('周长为 %d ' % t.permiter())
        print('面积为 %d ' % t.area())
    else:
        print('无法构成三角形！')


if __name__ == '__main__':
    main()

