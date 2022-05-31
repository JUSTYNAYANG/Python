from pycat.core import Window, Sprite, Color
from random import Random, randint

w = Window()

class Particle1(Sprite):
    def on_create(self):
        self.scale = 5
        self.time = 0
        self.speed = 2
        # self.color = C
    def on_update(self, dt):
        self.speed *= 0.99
        self.time += dt
        self.move_forward(self.speed)
        if self.time >= 1:
            for i in range(36):
                part1 = w.create_sprite(Particle2)
                part1.position = self.position
                part1.rotation = randint(0,360)
            self.delete()
        
class Particle2(Sprite): 
    def on_create(self):
        self.scale = 2
        self.time = 0   
    def on_update(self,dt):
        self.move_forward(2)
        self.time += dt
        if self.time > 2:
            self.delete()

class Creator(Sprite):
    def on_left_click_anywhere(self):
        for i in range(5):
            part = w.create_sprite(Particle1)
            part.position = w.mouse_position
            part.rotation = randint(70, 110)

w.create_sprite(Creator)

w.run()