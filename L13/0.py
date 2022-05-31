from random import randint
from pycat.core import Window, Sprite, Color

w = Window()

class Particle(Sprite):
    def on_create(self):
        self.goto_random_position()
        self.rotation = randint(0,360)
        self.scale = randint(5,20)
        self.set_random_color()
    def on_update(self, dt):
        self.move_forward(10)
        if self.is_touching_window_edge():
            # self.delete()
            self.rotation += 180
            


for i in range(100):
    w.create_sprite(Particle)

w.run()