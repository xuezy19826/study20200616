# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          14
# Description:   迭代器和生成器
# Author:        xuezy
# Date:          2020/12/8 11:07
# --------------------------------------------------------------
"""
和迭代器相关的魔术方法（__iter__ 和 __next__）
两种船舰生成器的方式：
（1）生成器表达式
（2）yield关键字
"""


def scq(num):
    """生成器"""
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        # yield相当于return，返回一个值，获取用next()
        yield a


class Fib(object):
    """迭代器"""
    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b , self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()


if __name__ == '__main__':
    # 调用生成器
    scq = scq(5)
    print(scq)
    print(" ******** ")
    # 1
    print(next(scq))
    print(" ******** ")
    # 1
    print(next(scq))

