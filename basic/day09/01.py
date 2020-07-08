# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          01
# Description:   @property包装器的使用 和 __slots__魔法
#                @property 表示getter方法
#                setter方法为修改器，用法： 方法上添加 @属性名.setter   参考下方  def age(self, age)
#
#                __slots__魔法：限制对象只能绑定某些属性，只对当前类生效，对子类不起作用
# Author:        xuezy
# Date:          2020/7/8 16:28
# --------------------------------------------------------------


class Person(object):

    # 限制Person对象只能绑定_name、_age 和 _gender属性
    # 若不绑定_age，报错：AttributeError: 'Person' object has no attribute '_age'
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 15:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('曹沫', 11)
    person.play()

    # 调用setter修改器，修改年龄
    person.age = 18
    person.play()
    # 没有添加setter修改器，不能修改，报错： AttributeError: can't set attribute
    # person.name = '王大锤'
    # person.play()


if __name__ == '__main__':
    main()
