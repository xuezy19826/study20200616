# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          03
# Description:   写入内容到文件
#                文件模式设置为：w，表示写入，追加设置为 a
# Author:        xuezy
# Date:          2020/7/10 17:25
# --------------------------------------------------------------
"""
1~99之间的素数写入a.txt
100~999之间的素数写入b.txt
1000~9999之间的素数写入c.txt
"""
from math import sqrt


def is_prime(n):
    """判断是否为素数"""
    # 断言，为True时正常执行，为False时抛出异常
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def main():
    filenames = ['a.txt', 'b.txt', 'c.txt']
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if number < 100:
                fs_list[0].write(str(number) + '\n')
            elif number < 1000:
                fs_list[1].write(str(number) + '\n')
            else:
                fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成')


if __name__ == '__main__':
    main()
