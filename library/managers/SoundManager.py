class SoundManager:
    PATH_TO_SOUNDS = "./data/sounds/"

    def __init__(self, main_log, fm):
        self.main_log = main_log
        self.fm = fm

        self.pygame = 0
        self.sounds = dict()

        self.load_all_sounds()

    def set_pygame(self, pygame):
        self.pygame = pygame
        self.main_log.write_log(f"Yes! I get the pygame", self)
        # getting the pygame object

    def load_all_sounds(self):
        pass
        # Im so lazzy .......

    def load_sound(self, name):
        if not self.pygame:
            self.main_log.write_log(f"No pygame", self, self.main_log.ERROR_STATE)
            return
        sound_object = self.pygame.mixer.Sound(self.PATH_TO_SOUNDS + name)
        self.sounds[name] = sound_object

    def play_sound(self, name):
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
        self.pygame.mixer.music.play(-1, 0.0)  # -1 means that this one will be endless,
        # 0.0 its time of begining of playing sound

    def stop_background_sound(self):
        if not self.pygame:
            self.main_log.write_log(f"No pygame", self, self.main_log.ERROR_STATE)
            return
        try:
            self.pygame.mixer.music.stop()
        except:
            self.main_log.write_log(f"Can't stop (may be no sound playing now)", self, self.main_log.ERROR_STATE)
