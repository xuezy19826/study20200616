# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          02
# Description:   使用列表 访问列表元素以及添加和删除列表元素操作
# Author:        xuezy
# Date:          2020/6/30 12:14
# --------------------------------------------------------------


def main():
    list1 = [1, 3, 5, 7, 1000]
    # [1, 3, 5, 7, 1000]
    print(list1)
    # ['hello', 'hello', 'hello', 'hello', 'hello']
    list2 = ['hello'] * 5
    print(list2)
    # 计算列表长度（元素个数）
    # 5
    print(len(list1))
    # 根据下标访问指定元素
    # 1
    print(list1[0])
    # 1000
    print(list1[4])
    # 倒数第一个元素  1000
    print(list1[-1])
    # 倒数第三个元素  5
    print(list1[-3])
    # 第三个元素赋值 200
    list1[2] = 200
    # [1, 3, 200, 7, 1000]
    print(list1)

    # 添加元素，默认追加在末尾
    list1.append(12)
    # [1, 3, 200, 7, 1000, 12]
    print(list1)
    # 第二个位置插入元素
    list1.insert(1, 13)
    # [1, 13, 3, 200, 7, 1000, 12]
    print(list1)
    # 添加列表
    list1 += [1001, 1002]
    # [1, 13, 3, 200, 7, 1000, 12, 1001, 1002]
    print(list1)
    # 9
    print(len(list1))
    # 删除元素(按照元素删除)
    list1.remove(3)
    # [1, 13, 200, 7, 1000, 12, 1001, 1002]
    print(list1)

    if 1 in list1:
        list1.remove(1)
    # [13, 200, 7, 1000, 12, 1001, 1002]
    print(list1)

    # 删除元素(按照索引删除)
    del list1[1]
    # [13, 7, 1000, 12, 1001, 1002]
    print(list1)

    # 删除元素(按照索引删除)并返回值  7
    a = list1.pop(1)
    print(a)

    # 清空列表
    list1.clear()
    # []
    print(list1)


if __name__ == '__main__':
    main()
