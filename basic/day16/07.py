# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          07.py    
# Description:   嵌套的列表
# Author:        xuezy
# Date:          2020/11/2421:32
# --------------------------------------------------------------


if __name__ == '__main__':
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    courses = ['语文', '数学', '英语']
    # 录入五个人的三门成绩
    scores = [[None] * len(courses) for _ in range(len(names))]
    for row, name in enumerate(names):
        for col, course in enumerate(courses):
            scores[row][col] = float(input(f'请输入{name}的{course}成绩：'))
            print(scores)
