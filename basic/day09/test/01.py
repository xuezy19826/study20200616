# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          01
# Description:   奥特曼打小怪兽
# Author:        xuezy
# Date:          2020/7/9 10:47
# --------------------------------------------------------------
from abc import ABCMeta, abstractmethod
from random import randint, randrange


class Fight(object, metaclass=ABCMeta):
    """ 父类：战斗者 """

    # 通过__slots__魔法限定对象可以绑定的成员变量
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        """
        初始化方法
        :param name: 名字
        :param hp:  生命值
        """
        self._name = name
        self._hp = hp

    # getter方法
    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    # 可以修改值的属性
    @hp.setter
    def hp(self, hp):
        self._hp = hp if self._hp > 0 else 0

    def alive(self):
        """ 判断是否有生命值 """
        return self._hp

    # 抽象方法，子类必须实现的方法
    @abstractmethod
    def attack(self, other):
        """
        攻击
        :param other: 被攻击的对象
        :return:
        """
        pass


class ultraman(Fight):
    """ 子类：奥特曼 """

    # 限定对象绑定的成员变量
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        """
        初始化方法
        :param name: 名字
        :param hp:   生命值
        :param mp:   魔法值
        """
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        """ 普通攻击（实现父类的抽象方法） """
        # 受到攻击后 生命值减少
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """
        究极必杀技（打掉对方至少50点或四分之三的血）
        :param other: 被攻击的对象
        :return: 使用成功返回True 否则返回False
        """
        # 魔法值>=50可以使用必杀技
        if self._mp >= 50:
            self._mp -= 50
            # 伤害值
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            # 普通攻击
            self.attack(other)
            return False

    def magic_attack(self, other):
        """
        魔法攻击
        :param other: 被攻击的小怪兽
        :return: 使用成功返回True 否则返回False
        """

        # 魔法值>=20 可以使用魔法攻击
        if self._mp >= 20:
            self._mp -= 20
            # 被攻击对象活着  减少生命值
            if other.alive() > 0:
                other.hp -= randint(15, 25)
            return True
        else:
            return False

    def resume(self):
        """ 恢复魔法值 """
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        """ 返回对象的描述信息 """
        return '~~~%s奥特曼~~~\n' % self._name + \
            '生命值：%d\n' % self._hp + \
            '魔法值：%d\n' % self._mp


class monster(Fight):
    """ 子类：小怪兽 """

    # 限定绑定的成员变量
    __slots__ = ('_name', '_hp')

    # 子类和父类的成员变量一致，没有必要再写初始化方法
    # def __init__(self, name, hp):
    #     super.__init__(name, hp)

    def attack(self, other):
        """
        攻击（实现父类的抽象方法）
        :param other:
        :return:
        """
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
            '生命值：%d\n' % self._hp


def is_any_alive(monsters):
    """ 判断有没有小怪兽是活着的 """
    for monster_one in monsters:
        if monster_one.alive() > 0:
            return True
    return False


def select_alive_one(monsters):
    """ 选中一只活着的小怪兽 """
    monsters_len = len(monsters)
    while True:
        # 随机选一只
        index = randrange(monsters_len)
        monster_one = monsters[index]
        if monster_one.alive() > 0:
            return monster_one


def display_info(ultraman, monsters):
    """ 显示奥特曼和小怪兽的信息 """
    print(ultraman)
    for monster in monsters:
        print(monster, end=' ')


def main():
    # 奥特曼
    u = ultraman('张三丰', 500, 120)
    # 小怪兽
    m1 = monster('狄仁杰', 100)
    m2 = monster('王大锤', 110)
    m3 = monster('陈友谅', 91)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive() > 0 and is_any_alive(ms):
        print('====================第%02d回合====================' % fight_round)
        # 选中一只小怪兽
        m = select_alive_one(ms)
        # 随机使用哪种攻击
        skill = randint(1, 10)
        # 60%概率使用普通攻击
        if skill <= 6:
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        # 30%的概率使用魔法攻击（可能因为魔法值不足失败）
        elif skill <= 9:
            if u.magic_attack(m):
                print('%s使用了魔法攻击%s.' % (u.name, m.name))
            else:
                print('%s使用魔法失败.' % u.name)
        # 10%的概率使用必杀技（如果魔法值不够使用普通攻击）
        else:
            if u.huge_attack(m):
                print('%s使用了必杀技攻击%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))

        # 如果小怪兽没有死，回击奥特曼
        if m.alive() > 0:
            print('%s回击了%s.' % (m.name, u.name))
            m.attack(u)

        # 每个回合结束，回显奥特曼和小怪兽信息
        display_info(u, ms)
        fight_round += 1
    print('\n==========战斗结束==========\n')
    if u.alive() > 0:
        print('%s奥特曼胜利！' % u.name)
    else:
        print('小怪兽胜利！')


if __name__ == '__main__':
    main()



