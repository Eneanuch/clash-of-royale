class SimpleVars:
    MAIN_MENU_STATUS = 0
    BATTLE_STATUS = 1
    BATTLE_KD_FOR_ELIXIR = 30

    def __init__(self, main_log, fm):
        main_log.write_log("Vars loaded", self)
