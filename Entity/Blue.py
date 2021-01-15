from pygame.sprite import AbstractGroup
from Entity.Entity import Entity


class Blue(Entity):
    def __init__(self, x, y, fm, bs, team_id, *groups: AbstractGroup):
        super().__init__(x, y, fm, bs, team_id, *groups)
        self.damage = 8
        self.max_hp = 60
        self.time_space = 15
        self.speed = 8
        self.price = 2.0

        self.image_name = 'blue.png'
        self.all_animations = ['walk', 'attack']
        self.all_animations_sprites = [6, 6]
        self.sprite_init()
