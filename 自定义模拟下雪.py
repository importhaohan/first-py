import pygame
import random

# 初始化 Pygame，调用该函数会初始化 Pygame 的所有模块，如显示、声音等
pygame.init()

width, height = 800, 600
# 创建一个指定尺寸的游戏窗口，返回一个 Surface 对象代表该窗口，后续的绘制操作都会在这个窗口上进行
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("自定义下雪模拟")

# 定义白色的 RGB 值，用于表示雪花的颜色，RGB 值范围是 0 - 255
WHITE = (149, 156, 158)
# 定义黑色的 RGB 值，用于表示背景颜色
BLACK = (0, 5, 15)

# 创建一个空列表，用于存储所有雪花的信息，每个雪花信息用一个子列表表示
snowflakes = []
# 定义雪花的数量，这里设置为 100 个
num_snowflakes = 100

# 初始化雪花，通过循环创建指定数量的雪花
for _ in range(num_snowflakes):
    # 随机生成雪花的 x 坐标，范围是从 0 到窗口的宽度
    x = random.randint(0, width)
    # 随机生成雪花的 y 坐标，范围是从 0 到窗口的高度
    y = random.randint(0, height)
    # 随机生成雪花的下落速度，范围是 1 到 5 之间的整数
    speed = random.randint(1, 5)
    # 随机生成雪花的大小，范围是 1 到 3 之间的整数
    size = random.randint(1, 3)
    # 将雪花的 x 坐标、y 坐标、下落速度和大小组成一个列表，并添加到雪花列表中
    snowflakes.append([x, y, speed, size])

# 创建一个 Clock 对象，用于控制游戏的帧率，确保游戏在不同性能的计算机上都能以相对稳定的速度运行
clock = pygame.time.Clock()
# 定义一个布尔变量，用于控制游戏主循环的运行，初始值为 True 表示游戏开始运行
running = True
# 游戏主循环，只要 running 为 True，循环就会一直执行
while running:
    # 遍历 Pygame 的事件队列，处理用户的输入事件，如鼠标点击、键盘按键、窗口关闭等
    for event in pygame.event.get():
        # 检查事件类型是否为窗口关闭事件（用户点击窗口的关闭按钮）
        if event.type == pygame.QUIT:
            # 如果是窗口关闭事件，将 running 设为 False，从而退出主循环
            running = False

    # 用黑色填充整个游戏窗口，相当于清空上一帧的画面，为绘制新的画面做准备
    screen.fill(BLACK)

    # 遍历雪花列表，对每个雪花进行位置更新和绘制操作
    for snowflake in snowflakes:
        # 更新雪花的 y 坐标，使其向下移动，移动的距离等于其下落速度
        snowflake[1] += snowflake[2]
        # 检查雪花是否落到了屏幕底部（y 坐标超过窗口高度）
        if snowflake[1] > height:
            # 如果落到屏幕底部，将雪花的 y 坐标重置为 0，使其重新从顶部开始下落
            snowflake[1] = 0
            # 随机生成一个新的 x 坐标，让雪花在顶部随机位置重新开始下落
            snowflake[0] = random.randint(0, width)
        # 在屏幕上绘制雪花，使用白色绘制一个圆形，圆心坐标为雪花的 x 和 y 坐标，半径为雪花的大小
        pygame.draw.circle(screen, WHITE, (snowflake[0], snowflake[1]), snowflake[3])

    # 更新整个游戏窗口的显示，将之前在屏幕上绘制的内容显示出来
    pygame.display.flip()
    # 控制游戏的帧率为 30 帧每秒，确保游戏运行的流畅度
    clock.tick(30)

pygame.quit()