from pygame.sprite import Sprite


class Elixir(Sprite):
    def __init__(self, fm, pg, screen, *group):
        super().__init__(*group)
        self.elixir = fm.get_function("SimpleVars").MAX_ELIX

        self.pg = pg
        self.fm = fm
        self.screen = screen

        self.black_rect = self.pg.Rect(250, 300, self.fm.get_function("SimpleVars").MAX_ELIX * 30, 7)

        self.draw()

    def draw(self):
        self.image = self.pg.Surface([self.elixir * 30, 7])
        self.image.fill('red')
        self.rect = self.pg.Rect(250, 300, self.elixir * 30, 7)

    def set_elixir(self, elixir):
        self.elixir = elixir
        self.pg.draw.rect(self.screen, self.pg.Color(0, 0, 0), self.black_rect)
        self.draw()
