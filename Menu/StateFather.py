class StateFather:
    def __init__(self, screen, pg, fm):
        self.fm = fm
        self.pg = pg
        self.screen = screen
        self.texts = dict()
        self.translate = fm.get_function("TranslateManager")

    def update(self, event):
        # your code in module
        pass

    def draw(self, pygame):
        # your code in module
        pass

    def draw_text(self, pg, text, x, y, font="Comic Sans MS", size=30, color=(255, 255, 255)):
        # default drawing text
        my_font = pg.font.SysFont(font, size)
        text_surface = my_font.render(text, False, color)
        self.screen.blit(text_surface, (x, y))


