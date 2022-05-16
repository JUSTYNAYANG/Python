from pycat.core import Window, Sprite
from random import random, randint

window = Window()

class Sware(Sprite):
    def on_create(self):
        self.goto_random_position()
        self.scale = randint(1, 100)
        self.opacity =  170
        self.set_random_color()

for _ in range(100):
    window.create_sprite(Sware)



window.run()