from pygame.sprite import AbstractGroup, Sprite
from pygame.sprite import spritecollideany

class Entity(Sprite):
    image_name = "entity.png"

    def __init__(self, max_hp, damage, speed, time_space,
                 width, height, x, y, price, fm, bs, *groups: AbstractGroup):
        super().__init__(*groups)

        self.max_hp = max_hp
        self.hp = max_hp
        self.damage = damage
        self.speed = speed
        self.size = (width, height)

        self.x = x
        self.y = y

        self.fm = fm
        self.battle_state = bs

        self.life_state = 1

        self.time_space = time_space
        self.price = price

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
        self.hp = self.fm.get_function('SimpleFunctionsManger').not_round_round(self.hp, 0, self.max_hp)
        if self.hp == 0:
            self.life_state = 0
            self.kill()

    def update(self):
        self.check_death()
        # checking on collidate with emenies



