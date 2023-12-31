import pygame
import math


# 矩形碰撞
# 判断矩形（小车）和线段（墙）之间是否碰撞（某个角或者某条边）
def collided_rect(a, b):
    # 先存下小车矩形4个点的偏移量
    p = []
    for i, j in [(1, -1), (1, 1), (-1, 1), (-1, -1)]:
        # 将旋转后相对于中心点的偏移量存到二维数组中
        # 直接调用api，手写边界情况较多
        # 将长和宽缩小80%，更接近真实（但是车头会多出来一截，可以再加一个碰撞检测）
        t = pygame.Vector2(i * a.width / 2 * 0.8, j * a.height / 2 * 0.8).rotate(a.forward_angle)
        p.append(t + a.rect.center)  # 存下4个点偏移后的坐标

    for i in range(4):
        x = p[i]
        y = p[(i + 1) % 4]
        if b.rect.clipline(x, y):  # 判断walls是否与x和y组成的线段相交
            return True

    p.clear()
    # w不变，h变为0.2
    for i, j in [(1, -1), (1, 1), (-1, 1), (-1, -1)]:
        t = pygame.Vector2(i * a.width / 2, j * a.height / 2 * 0.2).rotate(a.forward_angle)
        p.append(t + a.rect.center)  # 存下4个点偏移后的坐标

    for i in range(4):
        x = p[i]
        y = p[(i + 1) % 4]
        if b.rect.clipline(x, y):  # 判断walls是否与x和y组成的线段相交
            return True
        return False


# 只需判断车跟星星中心是否小于一个值？
def collided_circle(a, b):
    x1, y1 = a.rect.center
    x2, y2 = b.rect.center
    dx, dy = x1 - x2, y1 - y2
    if math.sqrt(dx * dx + dy * dy) < 50:
        return True
    return False
