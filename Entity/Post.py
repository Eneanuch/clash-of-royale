from pygame.sprite import AbstractGroup
from random import randint
from Entity.Entity import Entity


class Post(Entity):
    def __init__(self, x, y, fm, bs, team_id, *groups: AbstractGroup):
        super().__init__(x, y, fm, bs, team_id, *groups)
        self.damage = 0
        self.max_hp = fm.get_function("SimpleVars").POST_HEALTH
        self.time_space = 20
        self.speed = 0

        # self.image_name = f"post{randint(0, 1)}.png"
        self.image_name = f"tower{team_id}.png"
        self.all_animations = ["idle"]
        self.all_animations_sprites = [1]
        self.sprite_init()

    def check_death(self):
        super().check_death()