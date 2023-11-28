import pygame
from player import Player
from wall import Wall
from utils.collide import collided_rect


# 统一管理player, wall等资源
class GameManager:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player()
        self.walls = pygame.sprite.Group()  # 墙不止一个可以创建一个组来维护
        wall = Wall(200, 200, 500, 5)  # 初始化
        wall.add(self.walls)  # 将wall加到walls组里

    def check_collide(self):  # 检测碰撞
        # 单个对象和组进行判断，false表示碰撞后组不会被删
        # 返回一个列表,空表示没有碰撞，会返回false
        if pygame.sprite.spritecollide(self.player, self.walls, False, collided=collided_rect):
            self.player.crash()

    def update(self):
        self.player.update()  # 画之前update一下，动起来
        self.check_collide()
        self.screen.blit(self.player.image, self.player.rect)  # 将image画到rect
        self.walls.update()  # 会自动调用组里面的每一个wall的update
        self.walls.draw(self.screen)  # 组调用draw，自动遍历组里所有对象，然后画到屏幕上