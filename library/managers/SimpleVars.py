class SimpleVars:
    MAIN_MENU_STATUS = 0
    BATTLE_STATUS = 1

    BATTLE_KD_FOR_ELIXIR = 30
    MAX_ELIX = 10

    PLAYER_TEAM_ID = 0
    ENEMY_TEAM_ID = 1

    POST_ID = 0



    def __init__(self, main_log, fm):
        main_log.write_log("Vars loaded", self)
