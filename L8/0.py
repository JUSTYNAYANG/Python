from pycat.core import Window, Sprite, Label, Color
window = Window()

class Clock(Label):
    def on_create(self):
        self.time = 0
        self.is_running = False

    def on_update(self, dt):
        if self.is_running:
            self.time += dt
        self.text = str(round(self.time,3))

class Play(Sprite):
    def on_create(self):
        self.scale = 100
        self.color = Color.GREEN
        self.x = window.width * 1/3
        self.y = window.height/2
    def on_left_click(self):
        clock.is_running = not clock.is_running

class Reset(Sprite):
    def on_create(self):
        self.scale = 100
        self.color = Color.RED
        self.x = window.width * 2/3
        self.y = window.height/2
    def on_left_click(self):
        clock.time = 0
        
clock = window.create_label(Clock)

window.create_sprite(Play)
window.create_sprite(Reset)

window.run()