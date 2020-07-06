# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          08
# Description:   使用字典：键值对格式存储，相当于java中的map
# Author:        xuezy
# Date:          2020/7/6 17:48
# --------------------------------------------------------------


def main():
    scores = {'张三': 11, '李四': 12, '王五': 13}
    # 通过键可以获取字典中对应的值
    # 11
    print(scores['张三'])
    # 遍历
    # 张三	--->	11
    # 李四	--->	12
    # 王五	--->	13
    for elem in scores:
        # \t表示空四个字符
        # 格式符： %s    字符串     %d    十进制整数
        print('%s\t--->\t%d' % (elem, scores[elem]))

    # 更新元素
    scores['李四'] = 15
    # 添加元素
    scores.update(赵六=18,崔七=19)
    # {'张三': 11, '李四': 15, '王五': 13, '赵六': 18, '崔七': 19}
    print(scores)

    # 获取指定元素，没有则取默认值
    print(scores.get('一', 60))

    # 删除字典元素,默认删除末尾的元素 ('崔七', 19)
    print(scores.popitem())
    # 根据键删除元素，返回删除的值，没有则返回默认值   33
    print(scores.pop('二', 33))
    # 11
    print(scores.pop('张三', 34))
    # {'李四': 15, '王五': 13, '赵六': 18}
    print(scores)

    # 清空字典
    scores.clear()
    # {}
    print(scores)


if __name__ == '__main__':
    main()
