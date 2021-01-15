from pygame.sprite import AbstractGroup, Sprite
from pygame.sprite import spritecollideany
from pygame import Rect
from pygame.transform import flip


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
        self.price = 2.0

        # sprite init
        self.image_name = "entity.png"

        self.sprite_width = 70
        self.sprite_height = 70

        self.all_animations = ["walk", "attack", "death"]
        self.all_animations_file = list()
        self.all_animations_sprites = [10, 10, 10]

        self.tick_of_animation = 0

        self.now_animation = 0

    def sprite_init(self):
        self.image = self.fm.get_function("IMGManager").load_image(self.image_name)
        self.rect = self.image.get_rect()
        self.cut_sheet(max(self.all_animations_sprites),
                       len(self.all_animations_sprites))
        self.rect.x = self.x
        self.rect.y = self.y

    def cut_sheet(self, columns, rows):
        self.rect = Rect(0, 0, self.sprite_width,
                         self.sprite_height)

        for j in range(rows):
            some_anim = list()
            for i in range(self.all_animations_sprites[j]):
                frame_location = (self.rect.w * i, self.rect.h * j)
                some_anim.append(self.image.subsurface(
                    Rect(frame_location, self.rect.size)))
            self.all_animations_file.append(some_anim)
        for k, i in enumerate(self.all_animations_file):
            for k1, j in enumerate(i):
                self.all_animations_file[k][k1] = flip(
                    self.all_animations_file[k][k1],
                    self.fm.get_function("SimpleVars").PLAYER_TEAM_ID == self.team_id,
                    False)
        self.on_full_load()

    def on_full_load(self):
        self.update(None)
        if self.team_id == self.fm.get_function("SimpleVars").PLAYER_TEAM_ID:
            self.battle_state.player_entity.add(self)
        else:
            self.battle_state.enemy_entity.add(self)

    def set_health(self, hp):
        self.hp = hp

    def add_health(self, hp):
        self.hp += hp

    def give_damage(self, dmg):
        if dmg:
            self.fm.get_function('SoundManager').play_sound('attack.mp3')
            self.hp -= dmg

    def attack(self, entity):
        entity.give_damage(self.damage)

    def check_death(self):
        self.hp = self.fm.get_function('SimpleFunctionsManager') \
            .not_round_round(self.hp, 0, self.max_hp)
        if self.hp == 0:
            self.life_state = 0
            if len(self.all_animations_file) > 2:
                self.now_animation = 2
            else:
                self.kill()

    def update(self, event):
        self.check_death()
        self.now_time += 1
        try:
            self.image = self.all_animations_file[self.now_animation][
                self.tick_of_animation % len(self.all_animations_file[self.now_animation])]
            if self.time_space == self.now_time:
                self.now_time = 0

                if self.now_animation == 0:
                    # for walk
                    collide_sprite = spritecollideany(self, self.battle_state.get_not_my_group(self.team_id))
                    # can to attack?
                    # print(collide_sprite.__class__.__name__)
                    if collide_sprite and self.damage:
                        collide_sprite.give_damage(self.damage)
                        if len(self.all_animations_file) > 1:
                            self.now_animation = 1
                            # change to attack
                        self.tick_of_animation = 0
                if self.now_animation == 0:
                    self.rect.x += self.speed \
                        if self.fm.get_function("SimpleVars").PLAYER_TEAM_ID == self.team_id \
                        else -self.speed
                if self.now_animation == 1:
                    # print("attack")
                    if self.tick_of_animation == len(self.all_animations_file[self.now_animation]) - 1:
                        self.now_animation = 0
                if self.now_animation == 2:
                    # change to kill
                    if self.tick_of_animation == len(self.all_animations_file[self.now_animation]) - 1:
                        self.kill()

                # changing sprite
                self.tick_of_animation += 1
        except Exception as e:
            self.fm.get_main_log().write_log(f" {e} || {self.now_animation} ", self, self.fm.get_main_log().ERROR_STATE)
