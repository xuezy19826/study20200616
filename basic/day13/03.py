# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          03
# Description:   多线程下载示例
# Author:        xuezy
# Date:          2020/8/4 16:56
# --------------------------------------------------------------
"""
在Python早期的版本中就引入了thread模块（ 现在名为_thread） 来实现多线程编程， 然而该模块过
于底层， 而且很多功能都没有提供， 因此目前的多线程开发我们推荐使用threading模块， 该模块对多
线程编程提供了更好的面向对象的封装
"""
from random import randint
from threading import Thread
from time import time, sleep


def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成，耗时%d秒.' % (filename, time_to_download))


def main():
    start = time()
    t1 = Thread(target=download, args=('Python从入门到精通.pdf',))
    t1.start()
    t2 = Thread(target=download, args=('Python手册.pdf',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('共耗时%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
