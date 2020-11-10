# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          03
# Description:   归并排序
# Author:        xuezy
# Date:          2020/11/10 20:49
# --------------------------------------------------------------


def merge_sort(items, comp=lambda x, y: x <= y):
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return meger(left, right, comp)


def meger(items, items2, comp):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    end_items = []
    index, index2 = 0, 0
    while index < len(items) and index2 < len(items2):
        if comp(items[index], items2[index2]):
            end_items.append(items[index])
            index += 1
        else:
            end_items.append(items2[index2])
            index2 += 1
    end_items += items[index:]
    end_items += items[index2:]
    return end_items


if __name__ == '__main__':
    items = [5, 1, 3, 7, 2, 8]
    items = merge_sort(items)
    for i in range(len(items)):
        print(items[i])
