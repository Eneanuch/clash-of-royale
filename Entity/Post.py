from pygame.sprite import AbstractGroup
from Entity.Entity import Entity


class Post(Entity):
    def __init__(self, x, y, fm, bs, team_id, *groups: AbstractGroup):
        super().__init__(x, y, fm, bs, team_id, *groups)
        self.damage = 0
        self.max_hp = fm.get_function("SimpleVars").POST_HEALTH
        self.time_space = 20
        self.speed = 0

        self.sprite_width = 150
        self.sprite_height = 150

        # self.image_name = f"post{randint(0, 1)}.png"
        self.image_name = f"tower{team_id}.png"
        self.all_animations = ["idle"]
        self.all_animations_sprites = [1]
        self.sprite_init()

        # rect for health
        self.full_hp_rect = self.battle_state.pg.Rect(0, 0, self.max_hp * 10, 7)
        self.hp_rect = self.battle_state.pg.Rect(0, 0, self.hp * 10, 7)

    def update(self, event):
        super().update(event)

        self.full_hp_rect = self.battle_state.pg.Rect(self.rect.x - 10,
                                                      self.rect.y + self.sprite_height + 10, self.max_hp * 10, 7)
        self.hp_rect = self.battle_state.pg.Rect(self.rect.x - 10,
                                                 self.rect.y + self.sprite_height + 10, self.hp * 10, 7)

        self.draw_health()

    def draw_health(self):
        self.battle_state.draw_rect_alpha(self.battle_state.pg.Color(0, 0, 0, 128), self.full_hp_rect)
        self.battle_state.draw_rect_alpha(self.battle_state.pg.Color(255, 0, 0), self.hp_rect)
