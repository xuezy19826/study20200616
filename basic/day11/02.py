# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          02
# Description:   按行读取文件内容
# Author:        xuezy
# Date:          2020/7/10 17:08
# --------------------------------------------------------------
import time


def main():
    # 一次性读取整个文件内容
    with open('desc.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('desc.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end=' ')
            time.sleep(0.5)
    print()

    # 读取文件：按行读取到列表中
    with open('desc.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main()
