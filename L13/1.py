
from random import randint
from pycat.core import Window, Sprite, Color

w = Window()

class Button(Sprite):
    def on_create(self,):
        self.scale = 100
        self.x = 100
        self.y = 100
        self.color = Color.AMBER
    def on_left_click(self,):
        particlle = w.get_sprites_with_tag("particle")
        for p in particlle:
            p.color = Color.AMBER

class Particle(Sprite):
    def on_create(self):
        self.add_tag("particle")
        self.goto_random_position()
        self.rotation = randint(0,360)
        self.scale = randint(5,20)
        self.set_random_color()
    def on_update(self, dt):
        self.move_forward(10)
        if self.is_touching_window_edge():
            self.rotation += 180
            
w.create_sprite(Button)

for i in range(100):
    w.create_sprite(Particle)

w.run()