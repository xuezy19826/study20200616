# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          01
# Description:
# Author:        xuezy
# Date:          2020/11/6 17:04
# --------------------------------------------------------------
import datetime


def showtime():
    dt = datetime.datetime.now() + datetime.timedelta(days=-1)
    dt2 = datetime.datetime.now() + datetime.timedelta(days=-2)
    dt3 = datetime.datetime.now() + datetime.timedelta(days=-3)
    dt4 = datetime.datetime.now() + datetime.timedelta(days=-4)
    dt5 = datetime.datetime.now() + datetime.timedelta(days=-5)
    dtList = []
    for i in range(1, 5):
        j = -1
        dtList.append(datetime.datetime.now() + datetime.timedelta(days=-i))

    for d in dtList:
        print(d)


def showArray():
    items = [3, 4, 1, 2, 5]
    for i in range(0, len(items), 2):
        print(items[i])


if __name__ == '__main__':
    # showtime()
    # print(datetime.datetime.now())
    showArray()
