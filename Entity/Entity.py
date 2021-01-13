from pygame.sprite import AbstractGroup, Sprite
from pygame.sprite import spritecollideany
from pygame import Rect

class Entity(Sprite):

    def __init__(self, x, y, fm, bs, team_id,
                 *groups: AbstractGroup):
        super().__init__(*groups)

        self.max_hp = 100
        self.hp = self.max_hp
        self.damage = 10
        self.speed = 1

        self.x = x
        self.y = y

        self.fm = fm
        self.battle_state = bs

        self.team_id = team_id
        self.life_state = 1

        # some with time
        self.time_space = 20
        self.now_time = 0

        # pricing
        self.price = fm.get_function("SimpleFunctionsManager").\
            not_round_round(2, 0, fm.get_function("SimpleVars").MAX_ELIX)

        # sprite init
        self.image_name = "entity.png"

        self.sprite_width = 50
        self.sprite_height = 50

        self.all_animations = ["walk", "attack", "death"]
        self.all_animations_file = list()
        self.all_animations_sprites = [10, 10, 10]

        self.tick_of_animation = 0

        self.now_animation = 0

        self.sprite_init()

    def sprite_init(self):
        self.image = self.fm.get_function("IMGManager").load_image(self.image_name)
        self.rect = self.image.get_rect()
        self.cut_sheet(max(self.all_animations_sprites),
                       len(self.all_animations_sprites))
        self.rect.x = self.x
        self.rect.y = self.y

    def cut_sheet(self, columns, rows):
        self.rect = Rect(0, 0, self.image.get_width() // columns,
                         self.image.get_height() // rows)

        for j in range(rows):
            some_anim = list()
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * i)
                some_anim.append(self.image.subsurface(
                    Rect(frame_location, self.rect.size)))
            self.all_animations_file.append(some_anim)

    def set_health(self, hp):
        self.hp = hp
        self.check_death()

    def add_health(self, hp):
        self.hp += hp
        self.check_death()

    def give_damage(self, dmg):
        if dmg:
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
            self.now_animation = 2

    def update(self):
        self.check_death()
        self.now_time += 1
        if self.time_space == self.now_time:
            self.now_time = 0
            if self.now_animation == 0:
                # for walk
                collide_sprite = spritecollideany(self, self.battle_state.get_not_my_group(self.team_id))
                # can to attack?
                if collide_sprite:
                    collide_sprite.give_damage(self.damage)
                    self.now_animation = 1
                    self.tick_of_animation = 0
            if self.now_animation == 1:
                if self.tick_of_animation == len(self.all_animations_file[self.now_animation]) - 1:
                    self.now_animation = 0
            if self.now_animation == 2:
                if self.tick_of_animation == len(self.all_animations_file[self.now_animation]) - 1:
                    self.kill()

            # changing sprite
            self.image = self.all_animations_file[self.now_animation][
                self.tick_of_animation % len(self.all_animations_file[self.now_animation])]
            self.tick_of_animation += 1



