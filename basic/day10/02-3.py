# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          02-3
# Description:   使用Pygame进行游戏开发：加载图像
# Author:        xuezy
# Date:          2020/7/9 18:09
# --------------------------------------------------------------
import pygame


def main():
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口 并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口标题
    pygame.display.set_caption('大球吃小球')
    # 设置窗口背景色（颜色是由红绿蓝三色组成的元组）
    screen.fill((255, 255, 255))
    # 通过指定的文件名加载图像
    ball_image = pygame.image.load('image/ball.png')
    # 在窗口上渲染图像
    screen.blit(ball_image, (50, 50))
    # 刷新当前窗口（渲染窗口将绘制的图像呈现出来）
    pygame.display.flip()
    running = True
    # 开启一个时间循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
