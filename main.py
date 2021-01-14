from library.Logging import MainLog
from library.managers import CFGManager, DBManager, FunctionManager, \
    IMGManager, TranslateManager, SoundManager, SimpleVars, StateManager, \
    SimpleFunctionsManager
from os import environ
from Menu.MainMenu import MainMenu
from Menu.BattleState import BattleState

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

DEBUG = True

print_logs = False
log_it = False

WIDTH, HEIGHT = 800, 400
NAME = "Clash of Royale"
VERSION = "3.8"
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
    battle_state = BattleState(screen, pygame, fm)

    sm = fm.get_function("StateManager")  # state manager
    sm.add_state(main_menu)
    sm.add_state(battle_state)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fm.get_function("CFGManager").write_var_to_cfg("sound", fm.get_function("SoundManager").get_volume())
                fm.get_function("CFGManager").write_var_to_cfg("lang", fm.get_function("TranslateManager").get_curr())
                running = False
            sm.get_state(sm.get_current_state()).update(event)
        sm.get_state(sm.get_current_state()).draw()
        clock.tick(fps)
        pygame.display.flip()
        screen.fill((0, 0, 0))
