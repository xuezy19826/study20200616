# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          02-5
# Description:   使用Pygame进行游戏开发：碰撞检测
# Author:        xuezy
# Date:          2020/7/9 18:22
# --------------------------------------------------------------
from enum import Enum, unique
from math import sqrt
from random import randint

import pygame


# 检测枚举是否唯一
@unique
class Color(Enum):
    """颜色"""
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """获取随机颜色"""
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


class Ball(object):
    """球"""

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        """初始化方法"""
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True


    def move(self, screen):
        """移动"""
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or \
            self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <=0 or \
            self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        """吃其他球"""
        if self.alive and other.alive and self != other:
            # 两点见距离：sqrt√(x1 - x2) ** 2 + （y1 - y2）** 2
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            # 两点间距离 小于 两个圆的半径和 说明重叠了，小球被吃掉
            if distance < self.radius + other.radius \
                and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        """在窗口上绘制球"""
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)


def main():
    """
    事件处理：
    可以在事件循环中对鼠标事件进行处理，通过事件对象的type属性可以判断事件类型，再通过pos属性可以获得鼠标点击的位置。键盘事件类似
    """

    # 定义用来装所有球的容器
    balls = []
    #初始化导入的pygame中的模块
    pygame.init()
    # 初始化窗口 并设置大小
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    running = True
    # 开启一个时间循环处理发生的事件
    while running:
        # 从消息队列中获取时间并对其进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # 处理鼠标事件
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 获取点鼠标的位置
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                # 点击鼠标的位置创建一个球
                ball = Ball(x, y, radius, sx, sy, color)
                # 将球添加到列表容器中
                balls.append(ball)
        screen.fill((255, 255, 255))
        # 去除容器中的球，如果没有被吃掉就绘制 被吃掉了就移除
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        # 每隔50毫秒改变球的位置 再刷新窗口
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            # 检查球有没有吃到其他球
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main()
