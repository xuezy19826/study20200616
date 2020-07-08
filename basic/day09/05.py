# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          05
# Description:   多态：通过abc 模块的 ABCMeta 元类和 abstractmethod 包装器来达到抽象类的效果
#                【如果一个类存在抽象方法，这个类就不能实例化（创建对象）】
# Author:        xuezy
# Date:          2020/7/8 19:09
# --------------------------------------------------------------
from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    """ 父类：宠物 """

    def __init__(self, nickname):
        self._nickname = nickname

    # 抽象方法，子类必须实现
    @abstractmethod
    def make_voice(self):
        """ 发出声音 """
        pass


class Dog(Pet):
    """ 子类：狗 """
    def make_voice(self):
        print('%s：汪汪 ' % self._nickname)


class Cat(Pet):
    """ 子类：猫 """
    def make_voice(self):
        print('%s：喵喵 ' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('小猫'), Dog('大狗')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
