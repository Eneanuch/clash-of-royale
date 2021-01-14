from pygame.sprite import AbstractGroup
from Entity.Entity import Entity


class Grib(Entity):
    def __init__(self, x, y, fm, bs, team_id, *groups: AbstractGroup):
        super().__init__(x, y, fm, bs, team_id, *groups)
        self.damage = 10
        self.max_hp = 80
        self.time_space = 20
        self.speed = 10

        self.image_name = '2nice.png'
        self.all_animations = ['walk', 'death', 'attack']
        self.all_animations_sprites = [6, 5, 4]
        self.sprite_init()
