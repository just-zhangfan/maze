import pygame
import config
from game_manager import GameManager


pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()

game_manager = GameManager(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 关闭窗口结束
            running = False

    screen.fill('black')
    game_manager.update()

    pygame.display.flip()  # 染完色更新一哈

    clock.tick(config.FPS)  # 每秒执行60次循环(帧)，通过while加函数实现60帧


pygame.quit()  # 回收资源