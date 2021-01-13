from Menu.StateFather import StateFather
from Entity.Post import Post
from Low_line.Elixir import Elixir
from Low_line.Choose_line import Choose_line


class BattleState(StateFather):
    def __init__(self, screen, pg, fm):
        super().__init__(screen, pg, fm)
        self.fm = fm

        self.enemy_entity = pg.sprite.Group()
        self.player_entity = pg.sprite.Group()
        self.low_line = pg.sprite.Group()

        self.player_post = Post(0, 70, fm, self, fm.get_function("SimpleVars").PLAYER_TEAM_ID, self.player_entity)
        self.enemy_post = Post(650, 70, fm, self, 1, self.player_entity)
        self.elixir = Elixir(self.player_entity)
        images = [f'{i + 1}pre.png' for i in range(4)]
        self.choose_line = [Choose_line(4, images, i, fm, self.low_line) for i in range(4)]
        self.choose_line[0].set_selected(True)

        self.now_wave = 1

        self.player_elix = 50
        self.bot_elix = 50

    def update(self, event):
        super().update(event)
        self.enemy_entity.update(event)
        self.player_entity.update(event)
        if event.type == self.pg.KEYUP:
            index = max([i.is_selected() for i in self.choose_line])
            self.choose_line[index].set_selected(False)
            if event.key == self.pg.K_RIGHT:
                index = (index + 1) % 4
                self.fm.get_function('SoundManager').play_sound('menu.mp3')
            elif event.key == self.pg.K_LEFT:
                index = (index - 1) % 4
                self.fm.get_function('SoundManager').play_sound('menu.mp3')
            self.choose_line[index].set_selected(True)

    def draw(self):
        super().draw()
        self.enemy_entity.draw(self.screen)
        self.player_entity.draw(self.screen)
        self.low_line.draw(self.screen)

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
