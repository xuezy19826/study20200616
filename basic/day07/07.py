# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          07
# Description:   使用集合：不允许有重复元素
# Author:        xuezy
# Date:          2020/7/6 16:10
# --------------------------------------------------------------


def main():
    set1 = {1, 2, 3, 3, 4}
    # {1, 2, 3, 4}
    print(set1)
    # 4
    print(len(set1))
    # 生成集合
    set2 = set(range(1, 10))
    # {1, 2, 3, 4, 5, 6, 7, 8, 9}
    print(set2)
    # 添加元素
    set1.add(4)
    # {1, 2, 3, 4}
    print(set1)
    # 添加或修改集合，不存在即添加新的元素；参数可以是元素或集合
    set2.update([11])
    # {1, 2, 3, 4, 5, 6, 7, 8, 9, 11}
    print(set2)
    # 添加：存在了不添加
    set2.update([11, 13, 14])
    # {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14}
    print(set2)
    # 移除元素：该方法不同于 remove() 方法，因为 remove() 方法在移除一个不存在的元素时会发生错误，而 discard() 方法不会。
    set2.discard(5)
    # {1, 2, 3, 4, 6, 7, 8, 9, 11, 13, 14}
    print(set2)
    # 使用remove要做判断，存在则删除，不然可能会出错
    if 2 in set2:
        set2.remove(2)
    # {1, 3, 4, 6, 7, 8, 9, 11, 13, 14}
    print(set2)
    # 遍历
    for elem in set2:
        # 1 3 4 6 7 8 9 11 13 14
        print(elem, end=' ')
    print()

    # 元组转换为集合，会去除重复元素
    set3 = set((1, 2, 2, 3))
    # {1, 2, 3}
    print(set3)

    # 列表转换为集合，会去除重复元素
    set4 = set([1, 3, 3, 5])
    # {1, 3, 5}
    print(set4)

    # ************************* 集合运算 *************************
    # set3  {1, 2, 3}
    # set4  {1, 3, 5}

    # 交集 {1, 3}
    print(set3 & set4)
    print(set3.intersection(set4))
    # 并集 {1, 2, 3, 5}
    print(set3 | set4)
    print(set3.union(set4))
    # 差集 {2}
    print(set3 - set4)
    print(set3.difference(set4))
    # 对称差（异或，只存在各自集合中的元素） {2, 5}
    print(set3 ^ set4)
    print(set3.symmetric_difference(set4))

    # 如果一个集合S2中的每一个元素都在集合S1中，且集合S1中可能包含S2中没有的元素，则集合S1就是S2的一个超集，反过来，S2是S1的子集。
    # 判断子集和超集
    set5 = {1, 2, 3}
    set6 = {1, 2, 3, 4}
    set7 = {1, 3, 5}
    # False
    print(set6 <= set5)
    print(set6.issubset(set5))
    # True
    print(set6 >= set5)
    print(set6.issuperset(set5))
    # False
    print(set5 <= set7)


if __name__ == '__main__':
    main()
