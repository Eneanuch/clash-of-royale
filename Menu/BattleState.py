from Menu.StateFather import StateFather


class BattleState(StateFather):
    def __init__(self, screen, pg, fm):
        super().__init__(screen, pg, fm)

        self.enemy_entity = pg.sprite.Group()
        self.player_entity = pg.sprite.Group()

        self.now_wave = 1

        self.player_elix = 50
        self.bot_elix = 50

    def spawn_entities(self):
        for i in range(self.now_wave):
           pass

    def update(self, event):
        super().update(event)

    def draw(self, pygame):
        pass
