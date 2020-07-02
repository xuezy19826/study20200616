# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          05
# Description:   生成列表
# Author:        xuezy
# Date:          2020/7/2 18:24
# --------------------------------------------------------------
import sys


def main():
    f = [x for x in range(1, 10)]
    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f)

    f2 = [x + y for x in 'ABCDE' for y in '123']
    # ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1', 'D2', 'D3', 'E1', 'E2', 'E3']
    print(f2)

    # 用列表的生成表达式语法创建列表容器（容器：列表、元组、字典与集合）
    # 用这种语法创建列表之后元素已经准备就绪，所以序号耗费较多的内存空间
    f3 = [x ** 2 for x in range(1, 10)]
    # 查看对象占用内存的字节数  100
    print(sys.getsizeof(f3))
    # [1, 4, 9, 16, 25, 36, 49, 64, 81]
    print(f3)

    # 创建一个生成器对象
    # 通过生成器获取到数据不占用额外的空间
    f4 = (x ** 2 for x in range(1, 10))
    # 64
    print(sys.getsizeof(f4))
    print(f4)
    for val in f4:
        # 1 4 9 16 25 36 49 64 81
        print(val, end=' ')




if __name__ == '__main__':
    main()