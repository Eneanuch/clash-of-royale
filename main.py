from library.Logging import MainLog
from library.managers import CFGManager, DBManager, FunctionManager, \
    IMGManager, TranslateManager, SoundManager
from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

DEBUG = True

print_logs = False
log_it = False

WIDTH, HEIGHT = 500, 700
NAME = "Clash of Royale"
VERSION = "0.84"
BUILD = "6"
STATUS = "betta"

if __name__ == '__main__':
    if DEBUG:
        print_logs = True
        log_it = True
    main_log = MainLog.MainLog(print_logs, log_it)
    fm = FunctionManager.FunctionManager(main_log, CFGManager.CFGManager, DBManager.DBManager,
                                         IMGManager.IMGManager, TranslateManager.TranslateManager,
                                         SoundManager.SoundManager)
    fm.get_function("IMGManager").set_pygame(pygame)

    pygame.init()
    pygame.display.set_caption(NAME + " v" + VERSION + " build " + BUILD + " " + STATUS)
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    screen.fill((0, 0, 0))
    running = True
    v = 100  # пикселей в секунду
    fps = 60  # кадров в секунду
    all_sprites = pygame.sprite.Group()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(fps)
        pygame.display.flip()
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        all_sprites.update(event)
