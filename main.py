import pygame
import config
from player import Player


pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()

player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 关闭窗口结束
            running = False

    screen.fill('black')
    player.update()  # 画小车之前update一下，动起来
    screen.blit(player.image, player.rect)  # 将image画到rect(需要先画图再画小车)
    pygame.display.flip()  # 染完色更新一哈

    clock.tick(config.FPS)  # 每秒执行60次循环(帧)，通过while加函数实现60帧


pygame.quit()  # 回收资源