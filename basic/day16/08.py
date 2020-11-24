# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          08.py    
# Description:   heapq、itertools等的用法
# Author:        xuezy
# Date:          2020/11/2421:40
# --------------------------------------------------------------
"""
从列表中找出最大的或最小的N个元素
堆结构（大根堆/小根堆）
"""
import heapq


if __name__ == '__main__':
    list1 = [32, 23, 21, 14, 87, 22, 79, 2]
    list2 = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.12},
        {'name': 'FB', 'shares': 200, 'price': 21.7},
        {'name': 'HPQ', 'shares': 35, 'price': 33.3},
        {'name': 'YHOO', 'shares': 45, 'price': 16.15},
        {'name': 'ACME', 'shares': 75, 'price': 93.13}
    ]

    # [87, 79, 32] 找出最大的 3个
    print(heapq.nlargest(3, list1))
    # [2]          找出最小的1个
    print(heapq.nsmallest(1, list1))
    # 找出最大的 2个
    # [{'name': 'AAPL', 'shares': 50, 'price': 543.12}, {'name': 'ACME', 'shares': 75, 'price': 93.13}]
    print(heapq.nlargest(2, list2, key=lambda x: x['price']))
    # 找出最小的2个
    # [{'name': 'HPQ', 'shares': 35, 'price': 33.3}, {'name': 'YHOO', 'shares': 45, 'price': 16.15}]
    print(heapq.nsmallest(2, list2, key=lambda x: x['shares']))


