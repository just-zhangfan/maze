import pygame
import config


class Player(pygame.sprite.Sprite):  # 小组件
    def __init__(self):
        super(Player, self).__init__()
        self.width = 100
        self.height = 50
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill('red')
        self.rect = self.image.get_rect()  # 取出矩形
        self.rect.center = (config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 2)  # 对齐地图中心


    def update(self):
        pass
