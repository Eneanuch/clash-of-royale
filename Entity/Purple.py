from pygame.sprite import AbstractGroup
from Entity.Entity import Entity


class Purple(Entity):
    def __init__(self, x, y, fm, bs, team_id, *groups: AbstractGroup):
        super().__init__(x, y, fm, bs, team_id, *groups)
        self.damage = 25
        self.max_hp = 150
        self.time_space = 20
        self.speed = 10
        self.price = 4

        self.image_name = 'purple.png'
        self.all_animations = ['walk', 'attack', 'death']
        self.all_animations_sprites = [6, 4, 5]
        self.sprite_init()
