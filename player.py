import pygame
import config
import math


class Player(pygame.sprite.Sprite):  # 小组件
    def __init__(self):
        super(Player, self).__init__()
        self.width = 100
        self.height = 50
        self.forward_angle = 60  # 转弯的角度（与x轴顺时针转动的角度）
        self.image_source = pygame.image.load('static/images/car.png').convert()
        self.image = pygame.transform.scale(self.image_source, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, -self.forward_angle)  # 这里参数是逆时针
        self.image.set_colorkey('black')  # 将小车的黑色变成透明
        self.rect = self.image.get_rect()  # 取出矩形
        self.rect.center = (config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 2)  # 对齐地图中心
        self.last_time = pygame.time.get_ticks()  # 返回当前时刻，单位ms
        self.delta_time = 0  # 相邻两帧之间的时间间隔

        self.move_velocity_limit = 220  # 设置移动速度上限
        self.move_velocity = 0  # 当前的移动速度
        self.move_acc = 600  # 每秒将速度增加600
        self.friction = 0.95  # 摩檫力

    def update_delta_time(self):
        cur_time = pygame.time.get_ticks()
        self.delta_time = (cur_time - self.last_time) / 1000  # 时间间隔，将ms转为s
        self.last_time = cur_time  # 更新

    def input(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            self.move_velocity += self.move_acc * self.delta_time
            self.move_velocity = min(self.move_velocity, self.move_velocity_limit)
        elif key_pressed[pygame.K_DOWN]:
            self.move_velocity -= self.move_acc * self.delta_time
            self.move_velocity = max(self.move_velocity, -self.move_velocity_limit)
        else:
            self.move_velocity = int(self.move_velocity * self.friction)  # 没按up时，一直*f，直到速度降为0

    def move(self):
        if self.move_velocity != 0:
            # math.cos要接收弧度，需要将角度转换为弧度(几分之pi形式)
            vx = self.move_velocity * math.cos(math.pi * self.forward_angle / 180)
            vy = self.move_velocity * math.sin(math.pi * self.forward_angle / 180)
            self.rect.x += vx * self.delta_time
            self.rect.y += vy * self.delta_time

    def update(self):
        self.update_delta_time()  # 每次update调用一次更新函数
        self.input()
        self.move()
