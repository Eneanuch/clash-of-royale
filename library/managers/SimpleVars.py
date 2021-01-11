class SimpleVars:
    MAIN_MENU_STATUS = 0
    BATTLE_STATUS = 1

    def __init__(self, main_log, fm):
        main_log.write_log("Vars loaded", self)
