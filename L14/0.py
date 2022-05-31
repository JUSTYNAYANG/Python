from pycat.core import Color, Sprite, Window, Scheduler, Label
from random import randint

window = Window()


class Score(Label):
    def on_create(self):
        self.text = "0"
        self.score = 0
    def on_update(self, dt):
        self.text = str(self.score)
# haven't add score every time enemy killed

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
        self.add_tag("pbullet")
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
        self.t = 0
        self.hp = 20
        self.enemy_time = 0
    def on_update(self,dt):
        self.move_forward(self.speed)
        self.enemy_time += dt
        if self.is_touching_any_sprite_with_tag("pbullet"):
            if self.hp > 0:
                self.hp -= 5
                self.opacity -= 30
            else:
                self.delete()
                score.score += 1
        if self.is_touching_window_edge():
            if self.t <= 2:
                self.t += dt
            else:
                self.delete()
        if self.enemy_time > 2:
            bullet = window.create_sprite(EnemyBullet)
            bullet.position = self.position
            bullet.point_toward_sprite(player)
            self.enemy_time = 0



def spawn_enemy():
    window.create_sprite(Enemy)

class EnemyBullet(Sprite):
    def on_create(self):
        self.scale = 10
        self.color = Color.CYAN
    def on_update(self, dt):
        self.move_forward(5)

#haven't added damage to player yet


Scheduler.update(spawn_enemy, delay=2)

score = window.create_label(Score)
player = window.create_sprite(Player)
window.run()