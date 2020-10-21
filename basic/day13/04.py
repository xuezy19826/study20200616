# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          04
# Description:   多线程下载示例2
# Author:        xuezy
# Date:          2020/8/4 17:12
# --------------------------------------------------------------
"""
通过继承 Thread 类的方式来创建自定义的线
程类， 然后再创建线程对象并启动线程
"""
from random import randint
from threading import Thread
from time import time, sleep


class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成，耗时%d秒.' % (self._filename, time_to_download))

def main():
    start = time()
    t1 = DownloadTask('Python从入门到精通.pdf')
    t1.start()
    t2 = DownloadTask('Python手册.pdf')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('共耗时%d秒.' % (end - start))


if __name__ == '__main__':
    main()

