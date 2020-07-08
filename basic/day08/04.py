# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          04
# Description:   定义一个类描述数字时钟
# Author:        xuezy
# Date:          2020/7/8 15:51
# --------------------------------------------------------------
import time

class Clock(object):
    """
    数字时钟
    """

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

    def run(self):
        """
        走字
        :return:
        """
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
        """
        显示时间
        :return:
        """
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


def main():
    clock = Clock(1, 23, 14)
    while True:
        print(clock.show())
        time.sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
