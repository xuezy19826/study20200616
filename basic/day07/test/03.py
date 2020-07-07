# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          03
# Description:   设计一个函数返回给定文件名的后缀名
# Author:        xuezy
# Date:          2020/7/6 18:54
# --------------------------------------------------------------


def main(filename, has_not=False):
    """
    设计一个函数返回给定文件名的后缀名
    :param name: 文件名（默认测试.jpg）
    :return: 文件后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_not else pos + 1
        return filename[index:]
    else:
        return ''


if __name__ == '__main__':
    print(main('23423423.jpg'))