class StateFather:
    def __init__(self, screen, pg, fm):
        self.fm = fm
        self.pg = pg
        self.screen = screen

        self.texts = dict()
        self.is_started = False

        self.translate = fm.get_function("TranslateManager")

        fm.get_main_log().write_log("Its loaded", self)

    def update(self, event):
        # your code in module
        pass

    def draw(self):
        # your code in module
        pass

    def stop_state(self):
        self.is_started = False

    def start_state(self):
        self.is_started = True

    def draw_text(self, pg, text, x, y, font="Comic Sans MS", size=30, color=(255, 255, 255)):
        # default drawing text
        my_font = pg.font.SysFont(font, size)
        text_surface = my_font.render(text, False, color)
        self.screen.blit(text_surface, (x, y))

    def draw_rect_alpha(self, color, rect, radius=0):
        shape_surf = self.pg.Surface(self.pg.Rect(rect).size, self.pg.SRCALPHA)
        self.pg.draw.rect(shape_surf, color, shape_surf.get_rect(), border_radius=radius)
        self.screen.blit(shape_surf, rect)

