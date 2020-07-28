# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          03
# Description:   类方法（使用注解@classmethod）
#                类方法的第一个参数约定名为cls，它代表的是当前类相关的信息的对象，
#                有这个参数可以获取和类相关的信息并且和创建出类的对象
# Author:        xuezy
# Date:          2020/7/8 17:45
# --------------------------------------------------------------
from time import time, localtime, sleep


class Clock(object):
    """ 数字时钟 """

    def __init__(self, hour=0, minute=0, second=0):
        """
        初始化方法
        :param hour: 小时
        :param minute: 分钟
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    # 类方法注解
    @classmethod
    def now(cls):
        # 获取当前时间
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """ 走表 """
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """ 显示当前时间 """
        print('%02d:%02d:%02d' % (self._hour, self._minute, self._second))


def main():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        # 展示时间
        clock.show()
        # 休眠1秒
        sleep(1)
        # 走表
        clock.run()


if __name__ == '__main__':
    main()
