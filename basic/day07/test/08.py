# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          08
# Description:   约瑟夫环问题
# 幸运的基督徒
# 有15个基督徒 和 15个非基督徒 在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里，
# 有个人想了个办法就是大家围成一圈，由某个人开始从1报数，报到9的人就扔到海里，它后面的人接着从1开始报数，
# 报到9的人继续扔到海里，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免遇难，问这些人最开始是怎么站的，
# 哪些位置是基督徒哪些位置是非基督徒。
# Author:        xuezy
# Date:          2020/7/7 18:52
# --------------------------------------------------------------
from random import randint


def main():

    all_person = [x for x in range(1, 31)]
    all_person2 = all_person
    temp_person = []
    print(all_person)
    total_size = len(all_person)
    # 基督徒
    jdt = []
    # 非基督徒
    not_jdt = []
    while total_size > 15:
        for index, elem in enumerate(all_person):
            if index == 8:
                temp_person = []
                not_jdt.append(all_person[index])
                temp_person += all_person[index + 1:]
                temp_person += all_person[0:index]
                all_person = temp_person
                total_size = len(all_person)
                break
    for i in all_person2:
        if i not in not_jdt:
            jdt.append(i)

    print('基督徒站位：', sorted(jdt))
    print('非基督徒站位：',sorted (not_jdt))


if __name__ == '__main__':
    main()
