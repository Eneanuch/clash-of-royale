from pygame import transform
from pygame.sprite import Sprite


class Choose_line(Sprite):
    def __init__(self, width, images, count, fm, *group):
        super().__init__(*group)
        self.width = width
        self.count = count

        self.little = fm.get_function("IMGManager").load_image(images[count])
        self.little = transform.scale(self.little, (50, 50))
        self.big = transform.scale(self.little, (60, 60))
        self.image = self.little
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 300 + 50 * count + 10 * count, 330
        self.selected = False

    def set_selected(self, selected):
        if selected:
            self.selected = True
            self.image = self.big
            self.rect.x -= 7
            self.rect.y -= 15
        else:
            self.selected = False
            self.image = self.little
            self.rect.x += 7
            self.rect.y += 15

    def is_selected(self):
        if self.selected:
            return self.count
        else:
            return -1
