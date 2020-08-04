# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          04
# Description:   拆分长字符串
# Author:        xuezy
# Date:          2020/8/4 16:00
# --------------------------------------------------------------
import re


def main():
    poem = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r',.，。', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    # ['床前明月光，疑是地上霜。举头望明月，低头思故乡。']
    print(sentence_list)


if __name__ == '__main__':
    main()
