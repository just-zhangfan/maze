import pygame


class Star(pygame.sprite.Sprite):
    def __init__(self, center_x, center_y):
        super(Star, self).__init__()
        self.image_source = pygame.image.load('static/images/star.png')
        self.image = pygame.transform.scale(self.image_source, (50, 50))
        self.image.set_colorkey('black')
        self.rect = self.image.get_rect()
        self.rect.center = (center_x, center_y)
        self.scale = 1  # 星星大小默认1倍
        self.scale_delta = 0.01  # 每一帧星星加0.01倍

    def update(self):
        self.scale += self.scale_delta
        # 不能一直变大
        if self.scale > 1.1 or self.scale < 0.9:
            self.scale_delta *= -1
        self.image = pygame.transform.scale(self.image_source, (50 * self.scale, 50 * self.scale))
        # 更新（但是是以左上角为锚点来变化的）
        # 存下当前rect的中心点
        center = self.rect.center
        # 再求下新image的rect，再将rect的center与center重合
        self.rect = self.image.get_rect()
        self.rect.center = center