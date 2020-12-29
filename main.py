from library.Logging import MainLog
from library.managers import CFGManager, DBManager, FunctionManager,\
    IMGManager, TranslateManager
import pygame

DEBUG = 0

print_logs = False
log_it = False


if __name__ == '__main__':
    if DEBUG:
        print_logs = True
        log_it = True
    main_log = MainLog.MainLog(print_logs, log_it)
    fm = FunctionManager.FunctionManager(main_log, CFGManager.CFGManager, DBManager.DBManager,
                                         IMGManager.IMGManager, TranslateManager.TranslateManager)
    fm.get_function("IMGManager").set_pygame(pygame)