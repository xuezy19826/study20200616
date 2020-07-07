# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          05
# Description:   计算指定年月日是这一年的第几天
# Author:        xuezy
# Date:          2020/7/7 11:49
# --------------------------------------------------------------


def is_leap_year(year):
    """
    判断是否为闰年
    :param year: 年份
    :return: 是闰年返回True 不是返回False
    """
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def which_day(year, month, day):
    """
    判断输入的日期是当年的第几天
    :param year: 年
    :param month: 月
    :param day: 日
    :return: 天数
    """
    # 拥有31天的月份
    day_31 = [1, 3, 5, 7, 8, 10, 12]

    # 2月 闰年29天 非闰年28天
    if month == 2:
        if is_leap_year(year):
            month_day = 29
        else:
            month_day = 28
    elif month in day_31:
        month_day = 31
    else:
        month_day = 30

    # 返回总天数
    return month_day + day


if __name__ == '__main__':
    year = int(input('请输入年份：'))
    leapYear = is_leap_year(year)
    month = int(input('请输入月份：'))
    while month > 12:
        month = int(input('月份应小于等于12,请重新输入月份：'))
    day = int(input('请输入日：'))
    while month == 2 and leapYear and day > 29:
        day = int(input('闰年2月天数应不大于29天，请重新输入日：'))
    while month == 2 and leapYear != True and day > 28:
        day = int(input('闰年2月天数应不大于28天，请重新输入日：'))

    print('%d年%d月%d日 是这一天中的第%d天' % (year, month, day, which_day(year, month, day)))
