# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          03
# Description:   替换字符串中的不良内容
# Author:        xuezy
# Date:          2020/8/4 15:56
# --------------------------------------------------------------
import re


def main():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔', '*', sentence, flags=re.IGNORECASE)
    # 你丫是*吗? 我*你大爷的. * you.
    print(purified)


if __name__ == '__main__':
    main()
