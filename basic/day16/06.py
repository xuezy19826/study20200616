# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          06.py    
# Description:   使用生成式（推导式）语法
# Author:        xuezy
# Date:          2020/11/2421:26
# --------------------------------------------------------------


if __name__ == '__main__':
    prices = {
        'AAPL': 191.88,
        'GOOD': 1186.96,
        'IBM': 149.24,
        'ORCL': 48.44,
        'ACN': 166.89,
        'FB': 208.09,
        'SYMC': 21.29
    }

    # 价格大于100的构造一个新的字典
    prices2 = {key: value for key, value in prices.items() if value > 100}
    print(prices2)
