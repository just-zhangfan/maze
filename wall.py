import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):  # 左上角坐标以及形状
        super(Wall, self).__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill('#40b6e0')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
