from pycat.core import Window, Sprite, RotationMode, Scheduler, Label, Player
from random import randint
window = Window(background_image="media/underwater_04.png")

sound = Player("media/hit.wav")

class Score(Label):
    def on_create(self):
        self.text = "0" 
        self.score = 0

    def on_update(self, dt):
        self.text = str(self.score)


label = window.create_label(Score)

class Spaceship(Sprite):
    def on_create(self):
        self.image = "media/saucer.png"
        self.scale = 0.25
        self.x = window.width/2
        self.y = window.height - self.height
        self.rotation_mode = RotationMode.RIGHT_LEFT
    
    def on_update(self, dt):
        self.move_forward(3)
        if self.x >= window.width - self.width or self.x <= self.width:
            self.rotation += 180


class Alien(Sprite):
    def on_create(self):
        self.image= "media/" + str(randint(1, 5)) + ".png"
        self.scale = 0.25
        self.x = self.width * 2/3
        self.y = self.height * 2/3
        self.is_clicked = False
        self.y_speed = 10
    def on_update(self, dt):
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_any_sprite():
            self.delete()
            label.score += 1
            sound.play()

        if self.is_clicked:
           self.y += 5
        else:
            self.x += 3
            self.y += self.y_speed
            self.y_speed -= 0.5
            if self.y <= self.height * 2/3:
                self.y_speed = randint(10, 15)
    def on_left_click(self):
        self.is_clicked = True

def create_alien():
    window.create_sprite(Alien)
    Scheduler.wait(randint(1, 5), create_alien)

window.create_sprite(Spaceship)

create_alien()

window.run()