class SoundManager:
    PATH_TO_SOUNDS = "./data/sounds/"

    def __init__(self, main_log, fm):
        self.main_log = main_log
        self.fm = fm

        self.pygame = 0
        self.sounds = dict()

        self.now_volume = 0.1
        self.effects = True

        self.load_all_sounds()

        self.load_sound_from_cfg()

    def load_sound_from_cfg(self):
        if self.pygame:
            self.now_volume = float(self.fm.get_function("CFGManager").read_var_from_cfg("sound", "0.1"))
            self.pygame.mixer.music.set_volume(float(self.now_volume))
            self.effects = int(self.fm.get_function("CFGManager").read_var_from_cfg("effects", "0"))

    def set_pygame(self, pygame):
        self.pygame = pygame
        self.main_log.write_log(f"Yes! I get the pygame", self)
        self.load_sound_from_cfg()
        self.load_all_sounds()
        # getting the pygame object

    def load_all_sounds(self):
        from os import listdir
        for i in listdir(self.PATH_TO_SOUNDS):
            self.load_sound(i)
        # loading all sounds in sound dir

    def load_sound(self, name):
        if not self.pygame:
            self.main_log.write_log(f"No pygame", self, self.main_log.ERROR_STATE)
            return
        self.pygame.mixer.music.set_volume(self.now_volume)
        sound_object = self.pygame.mixer.Sound(self.PATH_TO_SOUNDS + name)
        self.main_log.write_log(f"Sound has been loaded '{name}'", self)
        self.sounds[name] = sound_object

    def set_volume(self, volume):
        volume = self.fm.get_function('SimpleFunctionsManager').not_round_round(volume, 0, 1)
        volume = float(str(volume)[:4])
        # some action
        self.now_volume = volume
        # print(self.pygame.mixer.music.get_volume())
        self.pygame.mixer.music.pause()
        self.pygame.mixer.music.set_volume(volume)
        self.pygame.mixer.music.unpause()

    def add_volume(self, volume):
        self.now_volume += volume
        self.set_volume(self.now_volume)

    def remove_volume(self, volume):
        self.now_volume -= volume
        self.set_volume(self.now_volume)

    def get_volume(self):
        return str(self.now_volume)[:3]

    def play_sound(self, name):
        if self.effects:
            try:
                self.sounds[name].play()
            except:
                self.main_log.write_log(f"No sound '{name}' in dict", self, self.main_log.CANT_LOAD_STATE)

    def stop_sound(self, name):
        try:
            self.sounds[name].stop()
        except:
            self.main_log.write_log(f"Cant stop sound '{name}'", self, self.main_log.CANT_LOAD_STATE)

    def delete_sound(self, name):
        try:
            self.sounds.pop(name)
            self.main_log.write_log(f"Deleting sound {name}", self)
        except:
            self.main_log.write_log(f"Cant delete (may be no object '{name}')", self, self.main_log.CANT_LOAD_STATE)

    def play_background_sound(self, name):
        if not self.pygame:
            self.main_log.write_log(f"No pygame", self, self.main_log.ERROR_STATE)
            return
        try:
            self.pygame.mixer.music.stop()
        except:
            self.main_log.write_log(f"Can't stop (may be no sound playing now)", self, self.main_log.ERROR_STATE)
        self.pygame.mixer.music.load(self.PATH_TO_SOUNDS + name)
        self.pygame.mixer.music.play(-1, 0.0)
        # -1 means that this one will be endless,
        # 0.0 its time of begining of playing sound

    def stop_background_sound(self):
        if not self.pygame:
            self.main_log.write_log(f"No pygame", self, self.main_log.ERROR_STATE)
            return
        try:
            self.pygame.mixer.music.stop()
        except:
            self.main_log.write_log(f"Can't stop (may be no sound playing now)", self, self.main_log.ERROR_STATE)

    def revert_effect(self):
        self.effects = not self.effects

    def get_effect(self):
        return self.fm.get_function('TranslateManager').translate("yes") if self.effects \
            else self.fm.get_function('TranslateManager').translate("no")

    def get_effects_int(self):
        return int(self.effects)
