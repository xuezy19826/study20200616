# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          02
# Description:   冒泡排序：升序
# Author:        xuezy
# Date:          2020/11/10 20:27
# --------------------------------------------------------------


def bubble_sort(origin_items, comp=lambda x, y: x > y):
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


if __name__ == '__main__':
    items = [5, 4, 3, 7, 1, 9, 2]
    print(len(items))
    items = bubble_sort(items)
    for i in range(len(items)):
        print(items[i])
