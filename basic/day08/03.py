# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          03
# Description:   私有方法 可以通过改名就可以访问到，单下划线开头的名称(必须是单下划线 + 类名)表示属性是受保护的
# Author:        xuezy
# Date:          2020/7/8 15:26
# --------------------------------------------------------------


class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    # _Test 单下划线开头的名称(必须是单下划线 + 类名)表示属性是受保护的
    test._Test__bar()
    print(test._Test__foo)


if __name__ == '__main__':
    main()
