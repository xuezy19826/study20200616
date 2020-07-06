# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          04
# Description:   列表排序
# Author:        xuezy
# Date:          2020/7/2 18:15
# --------------------------------------------------------------


def main():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    list2 = sorted(list1)
    # ['apple', 'blueberry', 'internationalization', 'orange', 'zoo']
    print(list2)

    # 倒叙  默认reverse=False升序
    list3 = sorted(list1, reverse=True)
    # ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']
    print(list3)

    # 通过key关键字指定根据字符长度排序   升序
    list4 = sorted(list1, key=len)
    # ['zoo', 'apple', 'orange', 'blueberry', 'internationalization']
    print(list4)
    # 通过key关键字指定根据字符长度排序   降序
    list5 = sorted(list1, key=len, reverse=True)
    # ['internationalization', 'blueberry', 'orange', 'apple', 'zoo']
    print(list5)


if __name__ == '__main__':
    main()
