# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          09.py    
# Description:   迭代工具-排列/组合/笛卡尔积
# Author:        xuezy
# Date:          2020/11/2422:22
# --------------------------------------------------------------
import itertools


if __name__ == '__main__':
    print(itertools.permutations('ABCD'))
    print(itertools.combinations('ABCDE', 3))
    print(itertools.product('ABCD', '123'))
