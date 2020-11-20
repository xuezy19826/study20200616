# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          05
# Description:   折半查找
# Author:        xuezy
# Date:          2020/11/17 20:57
# --------------------------------------------------------------


def bin_search(items, key):
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1