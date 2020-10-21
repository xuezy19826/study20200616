# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          06
# Description:   临界资源2 对05.py进行修改，解决结果错误问题(添加锁)
# Author:        xuezy
# Date:          2020/8/4 17:48
# --------------------------------------------------------------
"""
运行05.py的程序， 结果让人大跌眼镜， 100个线程分别向账户中转入1元钱， 结果居然远远小于100元。
之所以出现这种情况是因为我们没有对银行账户这个“临界资源”加以保护， 多个线程同时向账户中存钱
时， 会一起执行到 new_balance = self._balance + money 这行代码， 多个线程得到的账户余额都
是初始状态下的 0 ， 所以都是 0 上面做了+1的操作， 因此得到了错误的结果。 在这种情况
下， “锁”就可以派上用场了。 我们可以通过“锁”来保护“临界资源”， 只有获得“锁”的线程才能访问“临
界资源”， 而其他没有得到“锁”的线程只能被阻塞起来， 直到获得“锁”的线程释放了“锁”， 其他线程才
有机会获得“锁”， 进而访问被保护的“临界资源”。 下面的代码演示了如何使用“锁”来保护对银行账户
的操作， 从而获得正确的结果
"""
from time import sleep
from threading import Thread, Lock


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁才能执行后续代码
        self._lock.acquire()
        try:
            # 计算存款后的余额
            new_balance = self._balance + money
            # 模拟受理存款业务需要0.01秒
            sleep(0.01)
            # 修改账号余额
            self._balance = new_balance
        finally:
            # 释放锁
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    # 创建100个存款的线程向同一个账号存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的线程执行完毕
    for t in threads:
        t.join()
    print('账户余额为：￥%d元' % account.balance)


if __name__ == '__main__':
    # 账户余额为：￥100元
    main()