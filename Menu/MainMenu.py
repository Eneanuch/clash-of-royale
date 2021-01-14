from Menu.StateFather import StateFather


class MainMenu(StateFather):
    def __init__(self, screen, pg, fm):
        super().__init__(screen, pg, fm)

        self.current_button = 0

        self.background_group = pg.sprite.Group()

        self.background_sprite = pg.sprite.Sprite(self.background_group)
        self.background_sprite.image = fm.get_function("IMGManager").load_image("back_default.png")
        self.background_sprite.rect = self.background_sprite.image.get_rect()
        self.background_sprite.rect.x = 0
        self.background_sprite.rect.y = 0

        self.buttons = ["play", "difficult",  "sound", "lang", "exit"]
        self.buttons_status = ["",
                               "self.fm.get_function('DiffManager').get_diff()",
                               "self.fm.get_function('SoundManager').get_volume()",
                               "self.fm.get_function('TranslateManager').get_now_lang()",
                               ""]
        self.actions = [self.play_action, self.diff_action, self.sound_action, self.lang_action, self.exit_action]

    def draw(self):
        self.background_group.draw(self.screen)

        self.draw_rect_alpha(self.pg.Color(0, 0, 0, 200), self.pg.Rect(120, 100, 300, len(self.buttons) * 35), 8)

        for k, i in enumerate(self.buttons):
            if self.current_button == k:
                color = (255, 0, 0)
            else:
                color = (255, 255, 255)
            if self.buttons_status[k]:
                self.draw_text(self.pg, str(eval(self.buttons_status[k])), 350, 100 + k * 30)
            self.draw_text(self.pg, self.translate.translate(i), 150, 100 + k * 30, color=color)

    def play_action(self, event):
        if event.key == self.pg.K_RETURN:
            self.fm.get_function('StateManager').set_state(self.fm.get_function('SimpleVars').BATTLE_STATUS)

    def diff_action(self, event):
        if event.key == self.pg.K_RIGHT:
            self.fm.get_function('DiffManager').add_diff(1)
            self.fm.get_function('SoundManager').set_volume(self.fm.get_function('SoundManager').now_volume)
            self.fm.get_function('SoundManager').play_sound('replace.mp3')
        elif event.key == self.pg.K_LEFT:
            self.fm.get_function('DiffManager').add_diff(-1)
            self.fm.get_function('SoundManager').set_volume(self.fm.get_function('SoundManager').now_volume)
            self.fm.get_function('SoundManager').play_sound('replace.mp3')

    def sound_action(self, event):
        if event.key == self.pg.K_RIGHT:
            self.fm.get_function('SoundManager').add_volume(0.1)
            self.fm.get_function('SoundManager').set_volume(self.fm.get_function('SoundManager').now_volume)
            self.fm.get_function('SoundManager').play_sound('replace.mp3')
        elif event.key == self.pg.K_LEFT:
            self.fm.get_function('SoundManager').remove_volume(0.1)
            self.fm.get_function('SoundManager').play_sound('replace.mp3')

    def lang_action(self, event):
        if event.key == self.pg.K_RIGHT:
            self.fm.get_function('TranslateManager').revert_language()
            self.fm.get_function('SoundManager').play_sound('replace.mp3')
        elif event.key == self.pg.K_LEFT:
            self.fm.get_function('TranslateManager').revert_language()
            self.fm.get_function('SoundManager').play_sound('replace.mp3')

    def exit_action(self, event):
        if event.key == self.pg.K_RETURN:
            exit()

    def update(self, event):
        if event:
            if event.type == self.pg.KEYUP:
                if event.key == self.pg.K_UP:
                    self.current_button -= 1
                    self.fm.get_function('SoundManager').play_sound('menu.mp3')
                elif event.key == self.pg.K_DOWN:
                    self.current_button += 1
                    self.fm.get_function('SoundManager').play_sound('menu.mp3')
                else:
                    self.actions[self.current_button](event)
                self.current_button = self.fm.get_function("SimpleFunctionsManager"). \
                    round_round(self.current_button, 0, len(self.buttons) - 1)
