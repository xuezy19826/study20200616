# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          05
# Description: 【Craps赌博游戏】
# 玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
# 如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
# 玩家再次要色子 如果摇出7点 庄家胜
# 如果摇出第一次摇的点数 玩家胜
# 否则游戏继续 玩家继续摇色子
# 玩家进入游戏时有1000元的赌注 全部输光游戏结束
# Author:        xuezy
# Date:          2020/6/24 16:28
# --------------------------------------------------------------
import random

# 资金
money = 1000

while money > 0:
    print('原始资金：%d' % money)
    while True:
        # 输光了，退出游戏
        if money == 0:
            print('没有资金了，游戏结束！')
            break
        dz = int(input("请下注："))
        if dz > money:
            print('下注资金 不能大于 剩余资金')
            continue
        elif dz <= 0:
            print('下注资金应大于0')
            continue
        else:
            # 两次摇骰子的和
            z = random.randint(1, 6) + random.randint(1, 6)
            print('第一次摇出的点数为：%d' % z)
            # 玩家胜
            if z == 7 or z == 11:
                money += dz
                print('玩家胜，剩余资金%d' % money)
            # 庄家胜
            elif z == 2 or z == 3 or z == 12:
                money -= dz
                print('庄家胜，剩余资金%d' % money)
            # 继续游戏
            else:
                while True:
                    z2 = random.randint(1, 6) + random.randint(1, 6)
                    print('继续游戏：摇出点数为：%d' % z2)
                    # 玩家再次摇色子 如果摇出7点 庄家胜
                    # 如果摇出第一次摇的点数 玩家胜
                    if z2 == 7:
                        money -= dz
                        print('庄家胜，剩余资金%d' % money)
                        break
                    elif z2 == z:
                        money += dz
                        print('玩家胜，剩余资金%d' % money)
                        break
                    else:
                        print('继续游戏：玩家再次摇色子 如果摇出7点 庄家胜，如果摇出第一次摇的点数 玩家胜')

