from os import path


class IMGManager:
    def __init__(self, main_log, fm):
        self.pygame = 0
        self.main_log = main_log
        self.fm = fm  # functions manager
        self.all_images = dict()

    def set_pygame(self, pygame):
        if not pygame:
            self.pygame = pygame
        else:
            self.main_log.write_log(f"Pygame have already set genius", self)
        # optimization (or it will be import twice)

    def load_image(self, name, colorkey=None):
        if not self.pygame:
            self.main_log.write_log(f"EEEEE davai ura pygame naxui ne nuzhen davai!!!! (pygame is not loaded)", self)
            return
        fullname = path.join('data', name)
        if self.all_images.get(fullname, 0):
            self.main_log.write_log(f"File '{fullname}' has already loaded", self)
            return self.all_images.get(fullname, 0)
        # if file is already loaded (optimization)
        if not path.isfile(fullname):
            self.main_log.write_log(f"File '{fullname}' not found", self)
        image = self.pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        self.all_images[fullname] = image
        return image
