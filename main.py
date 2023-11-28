import pygame
import config
from game_manager import GameManager


pygame.init()
pygame.mixer.init()  # 初始化声音
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()

# bgm
pygame.mixer.music.load('static/sounds/bgm.wav')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)  # 传-1表示循环播放

game_manager = GameManager(screen, 1)

running = True
success_time = -1  # 获胜时刻，-1表示没有获胜
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 关闭窗口结束
            running = False

    if success_time >= 0:
        if pygame.time.get_ticks() - success_time > 2000:  # 获胜已经等待2妙，就加载下一关
            has_next = game_manager.next_level()
            if not has_next:  # # 没有下一关，游戏结束
                break
            success_time = -1  # 将获胜时间清空

    screen.fill('black')
    if game_manager.update():  # 每一帧需要执行的直接统一调用(打包)
        success_time = pygame.time.get_ticks()  # 更新获胜时刻

    pygame.display.flip()  # 染完色更新一哈

    clock.tick(config.FPS)  # 每秒执行60次循环(帧)，通过while加函数实现60帧


pygame.quit()  # 回收资源