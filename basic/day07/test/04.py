# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          04
# Description:   设计一个函数返回传入的列表中最大和第二大的元素的值
# Author:        xuezy
# Date:          2020/7/6 19:13
# --------------------------------------------------------------


def main(x):
    # 判断参数x是否为列表
    if isinstance(x, list):
        lenx = len(x)
        if lenx >= 2:
            x.sort(reverse=True)
            print(x)
            return x[0], x[1]

        else:
            return '列表中元素个数过少，请保证列表中至少有两个元素'
    else:
        return '请保证输入的参数为列表'


if __name__ == '__main__':
    print(main([3, 5, 9, 1, 4]))
    # print(main([1]))
