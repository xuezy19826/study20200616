# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          13
# Description:   类与类之间的关系
# Author:        xuezy
# Date:          2020/12/2 20:03
# --------------------------------------------------------------
"""
is-a 关系：继承
has-a 关系：关联/聚合/合成
use-a 关系：依赖

例子：扑克游戏
经验：符号常量重视优于字面常量，枚举类型是定义符号常量的最佳选择
"""
import random
from enum import Enum, unique


@unique
class Suite(Enum):
    """花色"""

    SPADE, HEART, CLUB, DIAMOND = range(4)

    def __lt__(self, other):
        return self.value < other.value


class Card():
    """牌"""

    def __init__(self, suite, face):
        """初始化方法"""
        self.suite = suite
        self.face = face

    def show(self):
        """显示牌面"""
        suites = ['♠', '♥', '♣', '♦']
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]} {faces[self.face]}'

    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()


class Poker():
    """扑克"""
    def __init__(self):
        self.index = 0
        self.cards = [Card(suite, face)
                        for suite in Suite
                        for face in range(1, 14)
                      ]

    def shuffle(self):
        """洗牌"""
        random.shuffle(self.cards)
        self.index = 0

    def deal(self):
        """发牌"""
        card = self.cards[self.index]
        self.index += 1
        return card

    @property
    def has_more(self):
        return self.index < len(self.cards)


class Player():
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸一张牌"""
        self.cards.append(card)

    def sort(self, comp=lambda card: (card.suite, card.face)):
        """整理手上的牌"""
        self.cards.sort(key=comp)


def main():
    """主函数"""
    poker = Poker()
    poker.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    while poker.has_more:
        for player in players:
            player.get_one(poker.deal())
    for player in players:
        player.sort()
        print(player.name, end='：')
        print(player.cards)


if __name__ == '__main__':
    main()

