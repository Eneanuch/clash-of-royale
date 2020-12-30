class IMGManager:
    PATH_TO_IMAGES = "./data/images/"

    def __init__(self, main_log, fm):
        self.pygame = 0
        self.main_log = main_log
        self.fm = fm  # functions manager
        self.all_images = dict()

    def set_pygame(self, pygame):
        self.pygame = pygame
        self.main_log.write_log(f"Yes! I get the pygame", self)
        # optimization (or it will be import twice)

    def load_all_images(self):
        pass
        # Im very lazy....

    def load_image(self, name, colorkey=None, replace_file=False):
        from os import path
        if not self.pygame:
            self.main_log.write_log(f"EEEEE davai ura pygame naxui ne nuzhen davai!!!!"
                                    f" (pygame is not loaded)", self, self.main_log.ERROR_STATE)
            return
        fullname = path.join(self.PATH_TO_IMAGES, name)
        if self.all_images.get(fullname, 0) and not replace_file:
            self.main_log.write_log(f"File '{fullname}' has already loaded", self)
            return self.all_images.get(fullname, 0)
        # if file is already loaded (optimization)
        if not path.isfile(fullname):
            self.main_log.write_log(f"File '{fullname}' not found", self, self.main_log.CANT_LOAD_STATE)
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
