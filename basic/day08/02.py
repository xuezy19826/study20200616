# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          module02_field
# Description:   类属性访问权限：公有、私有（名称前面加两个下划线）
# Author:        xuezy
# Date:          2020/7/8 15:15
# --------------------------------------------------------------


class Test:

    # self.name表示name为公有属性
    # self.__foo表示foo为私有属性（属性前面加两个下划线）
    def __init__(self, foo, name):
        self.__foo = foo
        self.name = name

    # 私有方法（方法名称前加两个下划线）
    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello', '李四')
    # 报错，找不到私有方法：AttributeError: 'Test' object has no attribute '__bar'
    # test.__bar()
    # 报错，找不到私有属性：AttributeError: 'Test' object has no attribute '__foo'
    # print(test.__foo)
    # 李四  公有属性，可以正常执行
    print(test.name)


if __name__ == '__main__':
    main()
