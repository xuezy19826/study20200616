# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          12
# Description:   面向对象的相关知识
# Author:        xuezy
# Date:          2020/12/2 19:30
# --------------------------------------------------------------
"""
三大支柱：封装、继承、多态
例子：工资结算系统
经理月15000，程序员每小时200，销售员1800底薪加销售额5%提成
"""
from abc import  ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """员工（抽象类）"""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """结算月薪（抽象方法：子类必须实现）"""
        pass


class Manger(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super.__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour


class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0.0):
        self.sales = sales
        super.__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


class EmployeeFactory():
    """创建员工的工厂（工厂模式 - 通过工厂实现对象使用者和对象之就按的解耦合）"""

    def create(emp_type, *args, **kwargs):
        """创建员工"""
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manger(*args, ** kwargs)
        elif emp_type == 'P':
            emp = Programmer(*args, **kwargs)
        elif emp_type == 'S':
            emp = Salesman(*args, **kwargs)
        return emp


def main():
    """主函数"""
    emps = [
        EmployeeFactory.create('M', '曹操'),
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85),
        EmployeeFactory.create('S', '典韦', 123000)
    ]
    for emp in emps:
        print('%s: %.2f远' % (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()
