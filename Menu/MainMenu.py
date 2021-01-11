from Menu.StateFather import StateFather


class MainMenu(StateFather):
    def __init__(self, screen, pg, fm):
        super().__init__(screen, pg, fm)
        fm.get_main_log().write_log("Its loaded", self)

        self.current_button = 0
        self.buttons = ["play", "sound", "lang", "exit"]
        self.buttons_status = ["",
                               "self.fm.get_function('SoundManager').get_volume()",
                               "self.fm.get_function('TranslateManager').get_now_lang()",
                               ""]
        self.actions = [self.play_action, self.sound_action, self.lang_action, self.exit_action]

    def draw(self, pg):
        for k, i in enumerate(self.buttons):
            if self.current_button == k:
                color = (255, 0, 0)
            else:
                color = (255, 255, 255)
            if self.buttons_status[k]:
                self.draw_text(pg, str(eval(self.buttons_status[k])), 250, 150 + k * 30)
            self.draw_text(pg, self.translate.translate(i), 150, 150 + k * 30, color=color)

    def play_action(self, event):
        pass

    def sound_action(self, event):
        pass

    def lang_action(self, event):
        pass
        # if event.key == self.pg.K_

    def exit_action(self, event):
        if event.key == self.pg.K_RETURN:
            exit()

    def update(self, event):
        if event.type == self.pg.KEYUP:
            if event.key == self.pg.K_UP:
                self.current_button -= 1
            elif event.key == self.pg.K_DOWN:
                self.current_button += 1
            else:
                self.actions[self.current_button](event)
            self.current_button = self.fm.get_function("SimpleFunctionsManager"). \
                round_round(self.current_button, 0, len(self.buttons) - 1)