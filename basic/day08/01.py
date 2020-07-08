# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          module01_student
# Description:   定义类：使用class关键字
# Author:        xuezy
# Date:          2020/7/8 14:42
# --------------------------------------------------------------


class Student(object):

    # __init__ 是一个特殊的方法，用于在创建对象时进行初始化操作
    # 通过这个方法，可以为学生绑定name和age两个属性(self.name表示name属性是公有的，私有的格式为属性前面加两个下划线：self.__name)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习《%s》.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 也有使用驼峰命名法的
    def watch_movice(self):
        if self.age < 18:
            print('%s只能看《熊出没》.' % self.name)
        else:
            print('%s正在看大片' % self.name)


def main():
    """
    创建和使用对象
    :return:
    """
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('张三', 12)
    # 给对象发sutdy消息
    stu1.study('python100天从新手到大师')
    stu1.watch_movice()

    stu2 = Student('米粒', 18)
    stu2.study('粮食起源')
    stu2.watch_movice()


if __name__ == '__main__':
    main()

