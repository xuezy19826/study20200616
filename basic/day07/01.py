# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          01
# Description:   使用字符串
# Author:        xuezy
# Date:          2020/6/30 11:22
# --------------------------------------------------------------


def main():
    str = 'hello,world!'
    # 计算字符串长度   12
    print(str.__len__())
    print(len(str))
    # 首字母大写   Hello,world!
    print(str.capitalize())
    # 字符串大写   HELLO,WORLD!
    print(str.upper())
    # 查找字符 在 字符串中的位置  0表示第一个位置  -1 表示没有找到
    print(str.find('h'))
    print(str.find('asd'))
    # str.index('asd') 此种方式找不到子串会发生异常
    # 判断字符串已什么内容开始 正确返回True  错误返回False
    print(str.startswith('h'))
    # 判断字符串已什么内容结尾 正确返回True  错误返回False
    print(str.endswith('sdf'))
    # 将字符串以指定的宽度居中，并在两侧填充指定字符
    print(str.center(30, '*'))
    # 将字符串以指定宽宽度靠左，并在右侧填充指定字符
    print(str.ljust(30, '-'))
    # 将字符串以指定宽宽度靠右，并在左侧填充指定字符
    print(str.rjust(30, '+'))
    # 从字符串中取出指定位置的字符
    print(str[1])
    # 字符串切片（从指定的开始索引到指定的结束索引）
    # 从第一位开始截取一位        h
    print(str[0: 1])
    # 从第二位开始获取到最后一位  ello,world!
    print(str[1:])
    # 从第一位开始获取，每两位数截取  hlowrd
    print(str[::2])
    # 字符串倒叙                     !dlrow,olleh
    print(str[::-1])
    # 从倒数第三位获取，获取两位     ld
    print(str[-3:-1])
    # 从倒数第三位获取，获取一位     l
    print(str[-3:-2])
    # 是否由数字构成       False
    print(str.isdigit())
    # 是否由字母构成       False
    print(str.isalpha())
    # 是否由数字和字母构成：一个条件成立并且不好含其他字符 即 为 True       False
    print(str.isalnum())

    print("********************** str2 = '123'  start ********************")
    str2 = '123'
    # True
    print(str2.isdigit())
    # False
    print(str2.isalpha())
    # True
    print(str2.isalnum())
    print("********************** str2 = '123'  end ********************")

    print("********************** str3 = '1s'  start ********************")
    str3 = '1s'
    # False
    print(str3.isdigit())
    # False
    print(str3.isalpha())
    # True
    print(str3.isalnum())
    print("********************** str3 = '1s'  end ********************")

    # 不包含空格长度：11   左边两个空格  右边一个空格
    str4 = '  test@qq.com '
    # 去掉左边的空额   长度：12
    print(len(str4.lstrip()))
    # 去掉右边的空额   长度：13
    print(len(str4.rstrip()))
    # 去掉两侧的空额   长度：11
    print(len(str4.strip()))


main()

