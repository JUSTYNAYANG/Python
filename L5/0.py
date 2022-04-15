from pycat.core import Window, Sprite, KeyCode, Scheduler, RotationMode
from random import randint

window = Window(background_image="img/beach_03.png")

class Player(Sprite):
    def on_create(self):
        self.image = "img/cat.png"
        self.y = self.height/2
        self.x = window.width/2
        self.rotation_mode = RotationMode.RIGHT_LEFT
    def on_update(self, dt):
        if window.is_key_pressed(KeyCode.LEFT):
            self.rotation = 180
            self.x -= 5
        if window.is_key_pressed(KeyCode.RIGHT):
            self.rotation = 0
            self.x += 5


class Gem(Sprite):
    def on_create(self):
        self.image = "img/gem_shiny01.png"
        self.x = randint(0, window.width)
        self.y = window.height
        self.scale = 0.2
    def on_update(self, dt):
        self.y -= 2
        if self.is_touching_sprite(cat) or self.y <= 0:
            self.delete()

cat = window.create_sprite(Player)


def create_gem():
    window.create_sprite(Gem)

create_gem()

Scheduler.update(create_gem, 1)



window.run()