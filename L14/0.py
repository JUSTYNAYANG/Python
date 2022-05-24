from pycat.core import Color, Sprite, Window, Scheduler
from random import randint

window = Window()


class Player(Sprite):

    def on_create(self):
        self.color = Color.MAGENTA
        self.scale = 30
        self.speed = 10
        self.x = window.width/2
        self.y = window.height/2
        self.bullet = 0

    def on_update(self, dt):
        if window.is_key_pressed("w"):
            self.y += self.speed
        elif window.is_key_pressed("a"):
            self.x -= self.speed
        elif window.is_key_pressed("s"):
            self.y -= self.speed
        elif window.is_key_pressed("d"):
            self.x += self.speed
    def on_left_click_anywhere(self):
        if self.bullet < 5:
            window.create_sprite(PlayerBullet)
            self.bullet += 1
        else:
            window.create_sprite(PowerPlayerBullet)
            self.bullet = 0

class PlayerBullet(Sprite):
    def on_create(self):
        self.scale = 10
        self.color = Color.AMBER
        self.position = player.position
        self.speed = 5
        self.point_toward_mouse_cursor()
    def on_update(self, dt):
        self.move_forward(self.speed)
        if self.is_touching_window_edge():
            self.delete()

class PowerPlayerBullet(Sprite):
    def on_create(self):
        self.scale = 20
        self.color = Color.AMBER
        self.position = player.position
        self.speed = 10
        self.point_toward_mouse_cursor()
    def on_update(self, dt):
        self.move_forward(self.speed)
        if self.is_touching_window_edge():
            self.delete()

class Enemy(Sprite):
    def on_create(self):
        self.goto_random_position()
        self.rotation = randint(0,360)
        self.speed = 3
        self.scale = 30
        self.color = Color.CHARTREUSE
    def on_update(self,dt):
        self.move_forward(self.speed)
        if self.is_touching_window_edge():
            self.delete()

def spawn_enemy():
    window.create_sprite(Enemy)

Scheduler.update(spawn_enemy, delay=2)

player = window.create_sprite(Player)
window.run()