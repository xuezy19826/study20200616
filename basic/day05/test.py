# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          test
# Description:   引用不同模块的同名方法

# 导入自己写的模块时No module named
# 解决办法：你可以把Test目录设置为源目录，在目录上右键，然后如下设置 make diceroty as -->source root
# Author:        xuezy
# Date:          2020/6/28 17:20
# --------------------------------------------------------------

import module1 as m1
import module2 as m2

m1.foo()
m2.foo()

