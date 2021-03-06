from library.Logging import MainLog
from library.managers import CFGManager, DBManager, FunctionManager, \
    IMGManager, TranslateManager, SoundManager, SimpleVars, StateManager, \
    SimpleFunctionsManager, DiffManager
from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from Menu.MainMenu import MainMenu
from Menu.BattleState import BattleState

# do not for pep8, but it only one way to hide it

DEBUG = False

print_logs = False
log_it = False

WIDTH, HEIGHT = 800, 400
NAME = "Clash of Royale"
VERSION = "6.6"
BUILD = "6"
STATUS = "alpha"

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
                                         SimpleFunctionsManager.SimpleFunctionsManager,
                                         DiffManager.DiffManager)

    # initialization pygame
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption(NAME + " v" + VERSION + " build " + BUILD + " " + STATUS)

    # setting up pygame to managers
    fm.get_function("IMGManager").set_pygame(pygame)
    fm.get_function("SoundManager").set_pygame(pygame)

    # window icon
    icon = pygame.image.load('./data/images/icon.png')
    pygame.display.set_icon(icon)

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

    some_event = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fm.get_function("CFGManager").write_var_to_cfg(
                    "sound",
                    fm.get_function("SoundManager").get_volume())
                fm.get_function("CFGManager").write_var_to_cfg(
                    "lang",
                    fm.get_function("TranslateManager").get_curr())
                fm.get_function("CFGManager").write_var_to_cfg(
                    "effects",
                    str(fm.get_function("SoundManager").get_effects_int()))
                fm.get_function("DiffManager").save_diff()
                running = False
            some_event = event
        sm.get_state(sm.get_current_state()).update(some_event)
        some_event = None
        sm.get_state(sm.get_current_state()).draw()
        clock.tick(fps)
        pygame.display.flip()
        screen.fill((0, 0, 0))
