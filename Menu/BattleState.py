from Menu.StateFather import StateFather
from Entity import Post, Grib, Blue, Purple, Flying
from Low_line.Elixir import Elixir
from Low_line.Choose_line import Choose_line


class BattleState(StateFather):
    def __init__(self, screen, pg, fm):
        super().__init__(screen, pg, fm)
        from random import randint
        self.fm = fm

        self.end_status = -1

        self.now_time = 0

        self.diff = 0

        self.score = 0
        self.do_score = 0

        self.bot_kd = randint(150, 500)

        self.all_types_of_entities = [Grib.Grib, Blue.Blue, Purple.Purple, Flying.Flying]

        self.void_entity = pg.sprite.Group()

        self.enemy_entity = pg.sprite.Group()
        self.player_entity = pg.sprite.Group()
        self.low_line = pg.sprite.Group()
        self.background_group = pg.sprite.Group()

        self.player_post = Post.Post(10, 70, fm, self, fm.get_function("SimpleVars").PLAYER_TEAM_ID, self.void_entity)
        self.enemy_post = Post.Post(650, 70, fm, self, fm.get_function("SimpleVars").ENEMY_TEAM_ID, self.void_entity)

        self.elixir = Elixir(self.fm, self.pg, self.screen, self.player_entity)
        images = ['gribpre.png', 'purplepre.png', 'bluepre.png', 'flyingpre.png']
        self.choose_line = [Choose_line(4, images, i, fm, self.low_line) for i in range(4)]
        self.choose_line[0].set_selected(True)

        self.player_elix = 10.0

        self.background_sprite = pg.sprite.Sprite(self.background_group)
        self.background_sprite.image = fm.get_function("IMGManager").load_image("back_default.png")
        self.background_sprite.rect = self.background_sprite.image.get_rect()
        self.background_sprite.rect.x = 0
        self.background_sprite.rect.y = 0

    def update(self, event):
        super().update(event)
        self.now_time += 1
        if self.elixir.elixir < 10:
            self.elixir.set_elixir(self.elixir.elixir + 0.01)
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
                        if 150 <= pos[0] <= 400 and pos[1] <= 230:
                            now = [Grib.Grib, Purple.Purple, Blue.Blue, Flying.Flying]
                            index = max([i.is_selected() for i in self.choose_line])
                            price = [4.0, 4.0, 2.0, 5.0]
                            if self.elixir.elixir >= price[index]:
                                go = now[index](pos[0] - 35, pos[1] - 35, self.fm, self,
                                                self.fm.get_function("SimpleVars").PLAYER_TEAM_ID, self.void_entity)
                                self.elixir.set_elixir(self.elixir.elixir - go.price)

        if event:
            if event.type == self.pg.KEYDOWN:
                if event.key == self.pg.K_ESCAPE:
                    # if user want to exit
                    self.fm.get_function('StateManager'). \
                        remove_state(self.fm.get_function('SimpleVars').BATTLE_STATUS)
                    self.fm.get_function('StateManager'). \
                        add_state(BattleState(self.screen, self.pg, self.fm))
                    self.fm.get_function('StateManager'). \
                        set_state(self.fm.get_function('SimpleVars').MAIN_MENU_STATUS)

        if self.now_time == self.bot_kd:
            from random import choice, randint
            # bot intelligent
            self.score += self.fm.get_function("SimpleVars").SCORE_ADDING * self.diff // 2
            for i in range(int(self.diff // 3)):
                en_entity = choice(self.all_types_of_entities)
                x, y = randint(500, 600), randint(30, 200)
                en_entity(x, y, self.fm, self, self.fm.get_function("SimpleVars").ENEMY_TEAM_ID)
                # расставляет в зависимости от расстановки врагов противника
            self.bot_kd = randint(150, 500)
            self.now_time = 0
        if not self.player_post.life_state:
            self.end_status = 1
            if not self.do_score:
                self.fm.get_function("DBManager"). \
                    do_request(f"INSERT INTO main (score) VALUES({self.score})")
                self.do_score = 1
        elif not self.enemy_post.life_state:
            self.end_status = 0
            if not self.do_score:
                self.fm.get_function("DBManager"). \
                    do_request(f"INSERT INTO main (score) VALUES({self.score})")
                self.do_score = 1

    def draw(self):
        super().draw()
        self.background_group.draw(self.screen)

        self.draw_rect_alpha(self.pg.Color(0, 0, 0, 200), self.pg.Rect(200, 270, 410, 125), 8)

        self.draw_text(
            self.pg,
            f"{self.fm.get_function('TranslateManager').translate('score')}:"
            f" {self.score}",
            10, 10, size=16)

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

    def start_state(self):
        super().start_state()
        self.diff = int(self.fm.get_function("DiffManager").get_diff())
        # print(self.diff)
        self.fm.get_function('SoundManager').play_background_sound('background_battle.mp3')

    def stop_state(self):
        super().stop_state()
        self.fm.get_function('SoundManager').play_background_sound('background_battle.mp3')
