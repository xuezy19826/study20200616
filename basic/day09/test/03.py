# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          03
# Description:   工资结算系统
# Author:        xuezy
# Date:          2020/7/9 15:38
# --------------------------------------------------------------
"""
某公司有三种类型的员工，分别是部门经理、程序员和销售员
需要设计一个工资结算系统，更具提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按照本月工作时间计算 每小时150元
销售员的月薪是1200远的底薪加上销售额5%的提成
"""
from abc import ABCMeta, abstractmethod


class Employee(object):
    """父类：员工"""

    def __init__(self, name):
        """初始化方法"""
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def month_money(self):
        """抽象方法，获取月工资"""
        pass


class Manage(Employee):
    """子类：部门经理"""

    def month_money(self):
        """获取月薪（实现父类的抽象方法）：固定15000元"""
        return 15000.0


class Programmer(Employee):
    """子类：程序员"""

    def __init__(self, name, work_time=0):
        """
        初始化方法
        :param name: 姓名
        :param work_time: 工作时长（以小时为单位）
        """
        super().__init__(name)
        self._work_time = work_time

    # getter方法
    @property
    def work_time(self):
        return self._work_time

    # setter方法
    @work_time.setter
    def work_time(self, work_time):
        self._work_time = work_time if work_time > 0 else 0

    def month_money(self):
        """获取月薪（实现父类的抽象方法）:工作时间长（单位：小时） * 150元 """
        return 150.0 * self._work_time


class BusinessManage(Employee):
    """子类：业务员"""

    def __init__(self, name, sales=0):
        """
        初始化方法
        :param name: 姓名
        :param sales: 营业额
        """
        super().__init__(name)
        self._sales = sales

    # getter方法
    @property
    def sales(self):
        return self._sales

    #setter方法
    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def month_money(self):
        """获取月薪（实现父类抽象方法）: 底薪1200 + 销售额 * 5% """
        return 1200 + self._sales * 0.05


def main():
    """填充好姓名及其它参数"""
    # 项目经理
    manage = Manage('杨老头')
    # 程序员
    programmers = [Programmer('程一', 172), Programmer('程二', 183), Programmer('程三', 194)]
    # 业务员
    businessManages = [BusinessManage('销售一', 100000), BusinessManage('销售二', 210000), BusinessManage('销售三', 230000)]
    # ============================== 月薪 ==============================
    print('项目经理 %s 月薪 %d' % (manage.name, manage.month_money()))

    for programmer in programmers:
        print('程序员 %s 月薪 %d' % (programmer.name, programmer.month_money()))

    for businessManage in businessManages:
        print('业务员 %s 月薪 %d' % (businessManage.name, businessManage.month_money()))


def main2():
    """手动输入参数"""
    emps = [Manage('刘备'), Programmer('诸葛亮'),
            Manage('曹操'), Programmer('荀彧'),
            BusinessManage('吕布'), BusinessManage('张辽'),
            Programmer('赵云')
            ]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.work_time = int(input('请输入%s本月工作时间（单位：小时）: ' % emp.name))
        elif isinstance(emp, BusinessManage):
            emp.sales = int(input('请输入%s本月销售额：' % emp.name))
        # 不同员工有不同的行为（工资计算方式，即多态）
        print('%s 本月工资为 ￥%s元' % (emp.name, emp.month_money()))


if __name__ == '__main__':
    # main()
    main2()