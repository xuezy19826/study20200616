# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          04
# Description:   顺序查找
# Author:        xuezy
# Date:          2020/11/17 20:54
# --------------------------------------------------------------


def seq_search(items, key):
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1


if __name__ == '__main__':
    items = [1, 4, 6, 2, 5]
    print(seq_search(items, 2))
