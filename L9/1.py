from pycat.core import Window, Sprite, Scheduler
from random import randint

WAIT = 1
ANGRY1 = 2
ANGRY2 = 3
THROW = 4



window = Window(is_sharp_pixel_scaling=True)

class WaitApe(Sprite):
    def on_create(self):
        self.x = window.width/2
        self.y = window.height/3
        self.scale = 7
        self.state = 1
        self.time = 0
        self.image = "img/ape_waiting.png"
    def on_update(self, dt):
        self.time += dt
        
        if self.state == WAIT:
            self.wait()

        elif self.state == ANGRY1:
            self.angry1()
        elif self.state == ANGRY2:
            self.angry2()
        else:
            self.throw()

    def wait(self):
        self.image = "img/ape_waiting.png"
        if self.time >= 2:
            self.state = ANGRY1
            self.time = 0
            self.a2 = 0
    def angry1(self):
        self.image = "img/ape_angry1.png"
        if self.time >= 0.5:
            self.state = ANGRY2
            self.time = 0
    def angry2(self):
        self.image = "img/ape_angry2.png"

        
        if self.time >= 0.5:
            if self.a2 >= 4:
                self.state = THROW
                self.time = 0
            else:
                self.state = ANGRY1
                self.a2 += 1
                self.time = 0

    def throw(self):
        window.create_sprite(Tomato)
        self.state = WAIT

class Tomato(Sprite):
    def on_create(self):
        self.image = "img/barrel1.png"
        self.position = wa.position
        self.rotation = randint(0,180)
        self.scale = 4
    def on_update(self, dt):
        self.move_forward(5)
        if self.is_touching_window_edge():
            self.delete()




wa = window.create_sprite(WaitApe)
window.run()