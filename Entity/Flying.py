from pygame.sprite import AbstractGroup
from Entity.Entity import Entity


class Flying(Entity):
    def __init__(self, x, y, fm, bs, team_id, *groups: AbstractGroup):
        super().__init__(x, y, fm, bs, team_id, *groups)
        self.damage = 70
        self.max_hp = 200
        self.time_space = 45
        self.speed = 8

        self.image_name = '4nice.png'
        self.all_animations = ['walk', 'death', 'attack']
        self.all_animations_sprites = [4, 5, 4]
        self.sprite_init()
