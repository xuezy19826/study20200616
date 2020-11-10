# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          01
# Description:   简单选择排序：升序
# Author:        xuezy
# Date:          2020/11/9 16:21
# --------------------------------------------------------------


def select_sort(origin_items, comp=lambda x, y: x < y):
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


if __name__ == '__main__':
    items = [4, 3, 6, 2, 5]
    items = select_sort(items)
    for i in range(len(items)):
        print(items[i])
