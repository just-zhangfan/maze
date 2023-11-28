import pygame
import config
from game_manager import GameManager
from utils.draw_text import draw_text


pygame.init()
# pygame.font.init()  # 初始化字体
pygame.mixer.init()  # 初始化声音
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()

# 自己的图标
ico = pygame.image.load('static/images/zf.ico').convert()
pygame.display.set_icon(ico)
pygame.display.set_caption("zf's game")

# bgm
pygame.mixer.music.load('static/sounds/bgm.wav')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)  # 传-1表示循环播放

game_manager = GameManager(screen, 1)

running = True
success_time = -1  # 当前管卡获胜时刻，-1表示没有获胜
success_finished = False  # 游戏是否已经通关
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 关闭窗口结束
            running = False
        elif success_finished and event.type == pygame.KEYDOWN:  # 已经通关，按下任意键结束
            running = False

    if success_finished:
        screen.fill('black')
        draw_text(screen, 'Win!', 200, config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 2)
    else:
        if success_time >= 0:
            if pygame.time.get_ticks() - success_time > 2000:  # 获胜已经等待2妙，就加载下一关
                has_next = game_manager.next_level()
                if not has_next:  # # 没有下一关，游戏结束
                    success_finished = True
                    continue
                success_time = -1  # 将获胜时间清空

        screen.fill('black')
        if game_manager.update():  # 每一帧需要执行的直接统一调用(打包)
            success_time = pygame.time.get_ticks()  # 更新获胜时刻

    pygame.display.flip()  # 染完色更新一哈
    clock.tick(config.FPS)  # 每秒执行60次循环(帧)，通过while加函数实现60帧


pygame.quit()  # 回收资源