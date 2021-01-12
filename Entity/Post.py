from pygame.sprite import AbstractGroup

from Entity.Entity import Entity


class Post(Entity):
    def __init__(self, x, y, fm, bs, team_id, *groups: AbstractGroup):
        super().__init__(x, y, fm, bs, team_id, *groups)
        self.dmg = 0
        self.max_hp = fm.get_function("SimpleVars").POST_HEALTH
        self.time_space = 20
        self.speed = 0

        self.image_name = "post.png"
        self.sprite_init()