# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          01
# Description:   读取文本文件（添加异常处理）
#    方式一：try except 抛出异常，finally释放资源
#    方式二：使用with关键字，自动释放资源，except 抛出异常
# Author:        xuezy
# Date:          2020/7/10 15:29
# --------------------------------------------------------------
import time


def main():
    """读取文件方式一：try except 抛出异常，finally释放资源"""
    f = None
    try:
        # 指定文件路径 编码
        f = open('desc.txt', encoding='utf-8')
        # 读取
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定文件')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')
    # 释放资源：方式一
    finally:
        if f:
            # 关闭
            f.close()


def main2():
    """读取文件方式二：使用with关键字，自动释放资源，except 抛出异常"""
    try:
        # 释放资源：方式二
        # 通过with 关键字指定文件对象的上下文环境 并在离开上下文环境时自定释放文件资源
        with open('desc.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定文件')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')


if __name__ == '__main__':
    # main()
    main2()
