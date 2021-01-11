from library.Logging import MainLog
from library.managers import CFGManager, DBManager, FunctionManager, \
    IMGManager, TranslateManager, SoundManager, SimpleVars, StateManager, \
    SimpleFunctionsManager
from os import environ
from Menu.MainMenu import MainMenu

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

DEBUG = False

print_logs = False
log_it = False

WIDTH, HEIGHT = 500, 700
NAME = "Clash of Royale"
VERSION = "0.84"
BUILD = "6"
STATUS = "betta"

if __name__ == '__main__':
    # debug setting
    if DEBUG:
        print_logs = True
        log_it = True
    # initialization main log file
    main_log = MainLog.MainLog(print_logs, log_it)

    # initialization FM
    fm = FunctionManager.FunctionManager(main_log, CFGManager.CFGManager, DBManager.DBManager,
                                         IMGManager.IMGManager, TranslateManager.TranslateManager,
                                         SoundManager.SoundManager, SimpleVars.SimpleVars,
                                         StateManager.StateManager,
                                         SimpleFunctionsManager.SimpleFunctionsManager)

    # initialization pygame
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption(NAME + " v" + VERSION + " build " + BUILD + " " + STATUS)

    # setting up pygame to managers
    fm.get_function("IMGManager").set_pygame(pygame)
    fm.get_function("SoundManager").set_pygame(pygame)

    # setting up the window
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    screen.fill((0, 0, 0))
    running = True
    fps = 60  # frames per sec

    main_menu = MainMenu(screen, pygame, fm)

    fm.get_function("StateManager").add_state(main_menu)
    sm = fm.get_function("StateManager")  # state manager
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            sm.get_state(sm.get_current_state()).update(event)
        sm.get_state(sm.get_current_state()).draw(pygame)
        clock.tick(fps)
        pygame.display.flip()
        screen.fill((0, 0, 0))
