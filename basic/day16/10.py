# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          10.py    
# Description:   collections模块下的工具类
# Author:        xuezy
# Date:          2020/11/2422:25
# --------------------------------------------------------------
"""
找出序列中出现次数最多的元素
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]

counter = Counter(words)
print(counter.most_common(3))

