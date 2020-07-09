# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          02-4
# Description:   使用Pygame进行游戏开发：实现动画效果
# Author:        xuezy
# Date:          2020/7/9 18:16
# --------------------------------------------------------------
import pygame


def main():
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口 并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口标题
    pygame.display.set_caption('大球吃小球')
    # 定义变量来表示小球在屏幕上的位置
    x, y = 50, 50
    running = True
    # 开启一个时间循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # 设置窗口背景色（颜色是由红绿蓝三色组成的元组）
        screen.fill((255, 255, 255))
        # 绘制一个圆（参数分别是：屏幕，颜色，圆心位置，半径，0表示填充圆
        pygame.draw.circle(screen, (255, 0, 0,), (x, y), 30, 0)
        # 刷新当前窗口（渲染窗口将绘制的图像呈现出来）
        pygame.display.flip()
        # 每隔50毫秒就改变小球的位置再刷新窗口
        pygame.time.delay(50)
        x, y = x + 5, y + 5


if __name__ == '__main__':
    main()
