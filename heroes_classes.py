class Hero:
    def __init__(self, level, damage, opportunities):
        self.level = level
        self.damage = damage
        self.opportunities = opportunities


class Jaba(Hero):
    def __init__(self, *args):
        super().__init__(*args)
        self.image = 'jaba.jpg'


class Bluster(Hero):
    def __init__(self, *args):
        super().__init__(*args)
        self.image = 'bluster.gif'


class Kica(Hero):
    def __init__(self, *args):
        super().__init__(*args)
        self.image = 'kica.jpg'


class Scary_Thing(Hero):
    def __init__(self, *args):
        super().__init__(*args)
        self.image = 'scary_thing.jpg'


class Clown(Hero):
    def __init__(self, *args):
        super().__init__(*args)
        self.image = 'clown.png'


class Dinosaur(Hero):
    def __init__(self, *args):
        super().__init__(*args)
        self.image = 'dinosaur.jpg'


class Wolf(Hero):
    def __init__(self, *args):
        super().__init__(*args)
        self.image = 'wolf.jpg'


class Mono_Eye(Hero):
    def __init__(self, *args):
        super().__init__(*args)
        self.image = 'mono_eye.jpg'


class Enemy:
    def __init__(self, level, damage, opportunities):
        self.level = level
        self.damage = damage
        self.opportunities = opportunities


class Alien(Enemy):
    def __init__(self, *args):
        super().__init__(*args)
        self.image = 'alien.jpg'


class Barmaglot(Enemy):
    def __init__(self, *args):
        super().__init__(*args)
        self.image = 'barmaglot.jpg'


class Devil(Enemy):
    def __init__(self, *args):
        super().__init__(*args)
        self.image = 'devil.jpg'


class Meh(Enemy):
    def __init__(self, *args):
        super().__init__(*args)
        self.image = 'meh.png'


class Sand_Monster(Enemy):
    def __init__(self, *args):
        super().__init__(*args)
        self.image = 'sand_monster.jpg'


class Octopus(Enemy):
    def __init__(self, *args):
        super().__init__(*args)
        self.image = 'octopus.jpg'


class The_Hand(Enemy):
    def __init__(self, *args):
        super().__init__(*args)
        self.image = 'the_hand.jpg'


class Triton(Enemy):
    def __init__(self, *args):
        super().__init__(*args)
        self.image = 'triton.jpg'


class Zhuzhalica(Enemy):
    def __init__(self, *args):
        super().__init__(*args)
        self.image = 'zhuzhalica.jpg'


class Zoombie(Enemy):
    def __init__(self, *args):
        super().__init__(*args)
        self.image = 'zoombie.jpg'
