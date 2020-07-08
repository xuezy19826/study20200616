# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          04
# Description:   继承
# Author:        xuezy
# Date:          2020/7/8 18:47
# --------------------------------------------------------------


class Person(object):
    """父类：人"""

    def __init__(self, name, age):
        """ 初始化方法 """
        self._name = name
        self._age = age

    # getter 获取方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # setter 修改发方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在玩耍' % self._name)

    def watch_tv(self):
        if self._age <= 18:
            print('%s只能看《熊出没》' % self._name)
        else:
            print('%s正在看大片' % self._name)


class Student(Person):
    """ 子类：学生，继承父类Person """

    def __init__(self, name, age, grade):
        """ 初始化方法，调用父类的初始化方法 """
        super().__init__(name, age)
        self._grade = grade

    # getter 获取方法
    @property
    def grade(self):
        return self._grade

    # setter 修改方法
    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s' % (self._grade, self._name, course))


class Teacher(Person):
    """ 子类：教师，继承父类Person """

    def __init__(self, name, age, title):
        """ 初始化方法，调用父类的初始化方法 """
        super().__init__(name, age)
        self._title = title

    # getter 获取方法
    @property
    def title(self):
        return self._title

    # setter 修改方法
    @title.setter
    def title(self, title):
        self._title = title

    def teacher(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))


def main():
    stu = Student('学生平安', 16, '初二')
    stu.study('高数')
    # 调用父类方法
    stu.watch_tv()

    t = Teacher('文圣', 351, '老秀才')
    t.teacher('三教论辩')
    t.watch_tv()


if __name__ == '__main__':
    main()
