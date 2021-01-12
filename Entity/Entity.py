from pygame.sprite import AbstractGroup, Sprite
from pygame.sprite import spritecollideany


class Entity(Sprite):
    image_name = "entity.png"

    def __init__(self, max_hp, damage, speed, time_space,
                 x, y, price, fm, bs, team_id,
                 *groups: AbstractGroup):
        super().__init__(*groups)

        self.max_hp = max_hp
        self.hp = max_hp
        self.damage = damage
        self.speed = speed

        self.x = x
        self.y = y

        self.fm = fm
        self.battle_state = bs

        self.team_id = team_id
        self.life_state = 1

        # some with time
        self.time_space = time_space
        self.now_time = 0

        # pricing
        self.price = fm.get_function("SimpleFunctionsManager").\
            not_round_round(price, 0, fm.get_function("SimpleVars").MAX_ELIX)

        # sprite init
        self.image = fm.get_function("IMGManager").load_image(self.image_name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_health(self, hp):
        self.hp = hp
        self.check_death()

    def add_health(self, hp):
        self.hp += hp
        self.check_death()

    def give_damage(self, dmg):
        self.fm.get_function('SoundManager').play_sound('attack.mp3')
        self.hp -= dmg
        self.check_death()

    def attack(self, entity):
        entity.give_damage(self.damage)

    def check_death(self):
        self.hp = self.fm.get_function('SimpleFunctionsManger')\
            .not_round_round(self.hp, 0, self.max_hp)
        if self.hp == 0:
            self.life_state = 0
            self.kill()

    def update(self):
        self.check_death()
        self.now_time += 1
        if self.time_space == self.now_time:
            self.now_time = 0
            collide_sprite = spritecollideany(self, self.battle_state.get_not_my_group(self.team_id))
            # can to attack?
            if collide_sprite:
                collide_sprite.give_damage(self.damage)
            # all check on everything



