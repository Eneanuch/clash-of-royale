from pygame.sprite import AbstractGroup
from Entity.Entity import Entity


class Flying(Entity):
    def __init__(self, x, y, fm, bs, team_id, *groups: AbstractGroup):
        super().__init__(x, y, fm, bs, team_id, *groups)
        self.damage = 10
        self.max_hp = 200
        self.time_space = 20
        self.speed = 5
        self.price = 5.0

        self.image_name = 'flying.png'
        self.all_animations = ['walk', 'death', 'attack']
        self.all_animations_sprites = [4, 4, 5]
        self.sprite_init()
