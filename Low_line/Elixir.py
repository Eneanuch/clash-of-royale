import pygame


class Elixir(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.elixir = 10
        self.draw()

    def draw(self):
        self.image = pygame.Surface([self.elixir * 60, 3])
        self.image.fill('red')
        self.rect = pygame.Rect(100, 270, self.elixir * 60, 3)

    def set_elixir(self, elixir):
        self.elixir = elixir
        self.draw()
