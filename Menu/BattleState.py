from Menu.StateFather import StateFather
from Entity.Post import Post
from Entity import Grib
from Low_line.Elixir import Elixir
from Low_line.Choose_line import Choose_line


class BattleState(StateFather):
    def __init__(self, screen, pg, fm):
        super().__init__(screen, pg, fm)
        self.fm = fm

        self.end_status = -1

        self.now_time = 0

        self.diff = int(fm.get_function("DiffManager").get_diff())
        self.bot_kd = 360 // self.diff

        self.enemy_entity = pg.sprite.Group()
        self.player_entity = pg.sprite.Group()
        self.low_line = pg.sprite.Group()
        self.background_group = pg.sprite.Group()

        self.player_post = Post(10, 70, fm, self, fm.get_function("SimpleVars").PLAYER_TEAM_ID, self.player_entity)
        self.enemy_post = Post(650, 70, fm, self, 1, self.player_entity)
        self.elixir = Elixir(self.player_entity)
        images = [f'{i + 1}pre.png' for i in range(4)]
        self.choose_line = [Choose_line(4, images, i, fm, self.low_line) for i in range(4)]
        self.choose_line[0].set_selected(True)

        self.player_elix = 50
        self.bot_elix = 50

        self.background_sprite = pg.sprite.Sprite(self.background_group)
        self.background_sprite.image = fm.get_function("IMGManager").load_image("background.png")
        self.background_sprite.rect = self.background_sprite.image.get_rect()
        self.background_sprite.rect.x = 0
        self.background_sprite.rect.y = 0

    def update(self, event):
        super().update(event)
        self.now_time += 1

        if self.end_status == -1:
            self.enemy_entity.update(event)
            self.player_entity.update(event)
            if event:
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
                if event.type == self.pg.MOUSEBUTTONDOWN:
                    pos = self.pg.mouse.get_pos()
                    if event.button == 1:
                        if pos[0] <= 400:
                            Grib.Grib(*pos, self.fm, self, self.fm.get_function("SimpleVars").PLAYER_TEAM_ID,
                                      self.player_entity)

        if self.now_time == self.bot_kd:
            for i in range(self.diff * 3):
                pass
            self.now_time = 0
        if not self.player_post.life_state:
            self.end_status = 1
        elif not self.enemy_post.life_state:
            self.end_status = 0

    def draw(self):
        super().draw()
        self.background_group.draw(self.screen)
        if self.end_status == -1:
            self.enemy_entity.draw(self.screen)
            self.player_entity.draw(self.screen)
            self.low_line.draw(self.screen)
        else:
            if self.end_status == self.fm.get_function("SimpleVars").PLAYER_WIN_STATE:
                win_text = self.translate.translate("player_win")
            else:
                win_text = self.translate.translate("player_lose")
            self.draw_text(self.pg, win_text, 270, 300)
            # draw win or lose text

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
