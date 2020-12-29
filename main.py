from library.Logging import MainLog
from library.managers import CFGManager, DBManager, FunctionManager,\
    IMGManager, TranslateManager
import pygame

DEBUG = 0

print_logs = 0
log_it = 0


if __name__ == '__main__':
    if DEBUG:
        print_logs = 1
        log_it = 1
    main_log = MainLog.MainLog(print_logs, log_it)
    fm = FunctionManager.FunctionManager(main_log, CFGManager.CFGManager, DBManager.DBManager,
                                         IMGManager.IMGManager, TranslateManager.TranslateManager)
    fm.get_function("IMGManager").set_pygame(pygame)