# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          02
# Description:   多线程下载示例2  使用multiprocessing模块的 Process 类来创建子进程
# Author:        xuezy
# Date:          2020/8/4 16:35
# --------------------------------------------------------------
from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    """
    下载文件
    :param filename: 文件
    :return:
    """
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成！耗时%d秒.' % (filename, time_to_download))


def main():
    start = time()
    # 通过 Process 类创建了进程对象
    p1 = Process(target=download_task, args=('Python从入门到精通.pdf',))
    # start 方法用来启动进程
    p1.start()
    p2 = Process(target=download_task, args=('Python手册.pdf',))
    p2.start()
    # join 方法表示等待进程执行结束
    p1.join()
    p2.join()
    end = time()
    print('共耗时%.2f秒' % (end - start))


if __name__ == '__main__':
    main()
