from pycat.core import Window, Sprite, Scheduler
from random import randint

window = Window(is_sharp_pixel_scaling=True)

class WaitApe(Sprite):
    def on_create(self):
        self.x = window.width/2
        self.y = window.height/3
        self.scale = 7
        self.wait()
        # Scheduler.wait(5,self.angry)
    def wait(self):
        self.image = "img/ape_waiting.png"
        Scheduler.wait(0.5,self.angry1)
        self.a2 = 0
    def angry1(self):
        self.image = "img/ape_angry1.png"
        Scheduler.wait(0.1, self.angry2)
    def angry2(self):
        self.image = "img/ape_angry2.png"
        if self.a2 < 4:
            Scheduler.wait(0.1,self.angry1)
            self.a2 += 1
        else:
            Scheduler.wait(0.1,self.throw)
    def throw(self):
        window.create_sprite(Tomato)
        Scheduler.wait(0.15,self.wait)

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