# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          04
# Description:   if语句
# Author:        xuezy
# Date:          2020/6/18 19:04
# --------------------------------------------------------------
import getpass

"""
用户身份验证
"""
username = input("请输入用户名：")
password = input("请输入口令：")
# 如果洗碗驶入口令时，终端不回显，使用getpass模块中的getpass函数

if username == 'admin' and password == '123':
    print('身份验证成功！')
else:
    print('身份验证失败！')

# 返回值为当前windows登陆用户名
usr = getpass.getuser()
print(usr)


"""
分段函数求值：
       3x - 5 (x > 1)
f(x) = x + 2 (-1 <= x <= 1)
       5x + 3 (x < -1)
"""
x = float(input('x = '))
if x < -1:
    y = 5 * x + 3
elif -1 <= x <= 1:
    y = x + 2
else:
    y = 3 * x - 5

print('f(%.2f) = %.2f' % (x, y))
