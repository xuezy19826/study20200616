# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          02
# Description:   设计一个函数产生指定长度的验证码，由大小写字母和数字构成
# Author:        xuezy
# Date:          2020/7/6 18:43
# --------------------------------------------------------------
import random


def generate_code(code_len=4):
    """
    生成指定长度的验证码
    :param code_len:验证码长度（默认4）
    :return: 由大小写字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # 字符串长度
    chars_len = len(all_chars) - 1

    code = ''
    for _ in range(code_len):
        index = random.randint(0, chars_len)
        code += all_chars[index]
    return code


if __name__ == '__main__':
    print(generate_code(5))
