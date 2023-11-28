import pygame


def draw_text(screen, text, size, x, y):
    font = pygame.font.SysFont(pygame.font.get_default_font(), size)
    image = font.render(text, True, 'white')  # 第二个参数是减少字体边界的锯齿感
    rect = image.get_rect()
    rect.center = (x, y)
    screen.blit(image, rect)
