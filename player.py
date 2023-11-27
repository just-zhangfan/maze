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
        self.last_time = pygame.time.get_ticks()  # 返回当前时刻，单位ms
        self.delta_time = 0  # 相邻两帧之间的时间间隔

    def update_delta_time(self):
        cur_time = pygame.time.get_ticks()
        self.delta_time = (cur_time - self.last_time) / 1000  # 时间间隔，将ms转为s
        self.last_time = cur_time  # 更新

    def update(self):
        self.update_delta_time()  # 每次update调用一次更新函数
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            self.rect.x += 200 * self.delta_time
        elif key_pressed[pygame.K_DOWN]:
            self.rect.x -= 200 * self.delta_time