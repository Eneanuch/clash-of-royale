from pygame.sprite import AbstractGroup
from Entity.Entity import Entity


class Grib(Entity):
    def __init__(self, x, y, fm, bs, team_id, *groups: AbstractGroup):
        super().__init__(x, y, fm, bs, team_id, *groups)
        self.damage = 10
        self.max_hp = 180
        self.time_space = 15
        self.speed = 3

        self.image_name = 'grib.png'
        self.all_animations = ['walk', 'attack']
        self.all_animations_sprites = [6, 4]
        self.sprite_init()
