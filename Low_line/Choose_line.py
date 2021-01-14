import pygame


class Choose_line(pygame.sprite.Sprite):
    def __init__(self, width, images, count, fm, *group):
        super().__init__(*group)
        self.width = width
        self.count = count
        self.little = fm.get_function("IMGManager").load_image(images[count])
        self.big = pygame.transform.scale(self.little, (110, 110))
        self.image = self.little
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 215 + 70 * count + 15 * count, 300
        self.selected = False

    def set_selected(self, selected):
        if selected:
            self.selected = True
            self.image = self.big
            self.rect.x -= 15
            self.rect.y -= 25
        else:
            self.selected = False
            self.image = self.little
            self.rect.x += 15
            self.rect.y += 25

    def is_selected(self):
        if self.selected:
            return self.count
        else:
            return -1
