# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          04
# Description:   读取二进制文件
# Author:        xuezy
# Date:          2020/7/10 17:58
# --------------------------------------------------------------


def main():
    try:
        # 读取二进制文件  r 读取  b 二进制模式
        with open('head.jpg', 'rb') as sf1:
            data = sf1.read()
            print(type(data))

        # 写入数据到二进制文件  w 写入  b 二进制模式
        with open('青蛙.jpg', 'wb') as sf2:
            sf2.write(data)

    except FileNotFoundError as e:
        print('无法打开指定文件')
        print(e)
    except IOError as e:
        print('读写文件错误')
        print(e)
    print('执行结束')


if __name__ == '__main__':
    main()
