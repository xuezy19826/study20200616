# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          02
# Description:   从一段文字中提取出国内手机号码
# Author:        xuezy
# Date:          2020/8/4 15:29
# --------------------------------------------------------------
import re


def main():
    # 创建正则
    pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍， 我的手机号是13512346789这个靓号，
    不是15600998765， 也是110或119， 王大锤的手机号才是15600998765。
    '''
    # 查找匹配的内容存到一个列表中
    my_list = re.findall(pattern, sentence)
    print(my_list)
    print('---------------- 分割线 -----------------------')
    # 通过迭代器去除匹配对象并获得匹配的内容
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('---------------- 分割线 -----------------------')
    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


if __name__ == '__main__':
    main()

