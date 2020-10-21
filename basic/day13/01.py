# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          01
# Description:   单线程下载示例
# Author:        xuezy
# Date:          2020/8/4 16:30
# --------------------------------------------------------------
from random import randint
from time import time, sleep


def download_task(filename):
    """
    下载文件
    :param filename: 文件名
    :return:
    """
    print('%s开始下载...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成，耗时%d秒' %(filename, time_to_download))


def main():
    start = time()
    download_task('Python从入门到精通.pdf')
    download_task('Python手册.pdf')
    end = time()
    print('共耗时%.2f秒' % (end - start))


if __name__ == '__main__':
    main()
