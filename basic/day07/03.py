# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          03
# Description:   列表切片
# Author:        xuezy
# Date:          2020/7/2 17:59
# --------------------------------------------------------------


def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 遍历元素
    for fruit in fruits:
        # .title() 返回"标题化"的字符串,就是说所有单词都是以大写开始
        # print默认是打印一行   end=' ' 表示末尾不换行
        # Grape Apple Strawberry Waxberry Pitaya Pear Mango
        print(fruit.title(), end=' ')
    print()

    # 列表切片
    # 从第二个元素开始获取，获取3个
    fruits2 = fruits[1:4]
    # ['apple', 'strawberry', 'waxberry']
    print(fruits2)

    # 通过完成的切片赋值列表
    fruits3 = fruits[:]
    # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
    print(fruits3)

    # 从倒数第三个元素开始，获取2个
    fruits4 = fruits[-3:-1]
    # ['pitaya', 'pear']
    print(fruits4)

    # 可以通过反向切换获取倒转后的列表
    fruits5 = fruits[::-1]
    # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']
    print(fruits5)


if __name__ == '__main__':
    main()
