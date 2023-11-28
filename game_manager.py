import pygame
from player import Player
from wall import Wall
from star import Star
from target import Target
from utils.collide import collided_rect


# 统一管理player, wall等资源
class GameManager:
    def __init__(self, screen, level):
        self.screen = screen
        self.level = level  # 加个关卡
        self.player = None
        self.walls = pygame.sprite.Group()  # 墙不止一个可以创建一个组来维护
        self.stars_cnt = 0  # 记录星星数量
        self.stars = pygame.sprite.Group()
        self.targets = pygame.sprite.Group()
        self.load()

    def load_walls(self, walls):
        self.walls.empty()  # 清空之前关卡
        for x, y, width, height in walls:
            wall = Wall(x, y, width, height)
            wall.add(self.walls)  # 不要写反了

    def load_stars(self, stars):
        self.stars.empty()
        for x, y in stars:
            star = Star(x, y)
            star.add(self.stars)

    def load_targets(self, targets):
        self.targets.empty()
        for x, y in targets:
            target = Target(x, y)
            target.add(self.targets)

    def load_player(self, center_x, center_y, forward_angle):
        if self.player:
            self.player.kill()  # 每次加载删掉之前的
        self.player = Player(center_x, center_y, forward_angle)

    # 加载当前这一关的地图信息
    def load(self):
        with open('static/maps/level1.txt', 'r') as fin:
            walls_cnt = int(fin.readline())
            walls = []
            for i in range(walls_cnt):
                x, y, width, height = map(int, fin.readline().split())
                walls.append((x, y, width, height))
            self.load_walls(walls)

            self.stars_cnt = int(fin.readline())
            stars = []  # 与self.stars不一样
            for i in range(self.stars_cnt):
                x, y = map(int, fin.readline().split())
                stars.append((x, y))
            self.load_stars(stars)

            targets_cnt = int(fin.readline())
            targets = []
            for i in range(targets_cnt):
                x, y = map(int, fin.readline().split())
                targets.append((x, y))
            self.load_targets(targets)

            center_x, center_y, forward_angle = map(int, fin.readline().split())
            self.load_player(center_x, center_y, forward_angle)

    def check_collide(self):  # 检测碰撞
        # 单个对象和组进行判断，false表示碰撞后组不会被删
        # 返回一个列表,空表示没有碰撞，会返回false
        if pygame.sprite.spritecollide(self.player, self.walls, False, collided=collided_rect):
            self.player.crash()

    def update(self):
        self.stars.update()
        self.stars.draw(self.screen)

        self.targets.update()
        self.targets.draw(self.screen)

        # 先画星星跟目标点，再画车
        self.player.update()  # 画之前update一下，动起来
        self.check_collide()
        self.screen.blit(self.player.image, self.player.rect)  # 将image画到rect
        self.walls.update()  # 会自动调用组里面的每一个wall的update
        self.walls.draw(self.screen)  # 组调用draw，自动遍历组里所有对象，然后画到屏幕上