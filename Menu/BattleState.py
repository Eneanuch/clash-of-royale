from Menu.StateFather import StateFather


class BattleState(StateFather):
    def __init__(self, screen, pg, fm):
        super().__init__(screen, pg, fm)

        self.enemy_entity = pg.sprite.Group()
        self.player_entity = pg.sprite.Group()

        self.now_wave = 1

        self.player_elix = 50
        self.bot_elix = 50

    def init_entities(self):
        for i in range(self.now_wave):
           pass

    def update(self, event):
        super().update(event)

    def draw(self):
        super().draw()

    def get_enemy_group(self):
        return self.enemy_entity

    def get_player_group(self):
        return self.player_entity

    def get_not_my_group(self, team_id):
        if team_id == self.fm.get_function("SimpleVars").PLAYER_TEAM_ID:
            return self.get_enemy_group()
        elif team_id == self.fm.get_function("SimpleVars").ENEMY_TEAM_ID:
            return self.get_player_group()
        else:
            return -1