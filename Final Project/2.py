from pycat.core import Window, Sprite, KeyCode, RotationMode, Color, Label
from random import randint
from pycat.experimental.simple_level_editor import start_level_editor
from level import generate_level

window = Window()

# generate_level(window, "Final Project/maze.py")
dotimage = ["img/dot-b.png", "img/dot-c.png"]

class Score(Label):
    def on_create(self):
        self.text = "100"
        self.score = 100
        self.t = 0
    def on_update(self, dt):
        self.text = str(int(self.score))
        if self.score <= 0:
            self.text = "                      YOU DIED......\n\n NO the DUCK DIED and it's YOUR FAULT"
            self.y = window.height/2
            self.x = window.width/2 - 300
            self.t += dt
            if self.t >= 10:
                window.close()
        if water.win == 1:
            self.text = "                      YAY\n\n      the duck got BACK HOME"
            self.y = window.height/2
            self.x = window.width/2 - 250
            self.t += dt
            if self.t >= 10:
                window.close()

class Duck(Sprite):
    def on_create(self):
        self.image_list = ["img/duck 1.png", "img/duck 2.png", "img/duck 3.png", "img/duck 4.png", "img/Tree1.png"]
        self.image = self.image_list[0]
        self.state = 0
        self.y = self.height / 2 + 20
        self.x = self.width / 2 + 20
        print(self.height / 2 + 20, self.width / 2 + 20)
        self.speed = 3
        self.scale = 0.7
        self.layer = 1
        self.add_tag("duck")

    def on_update(self,dt):
        if window.is_key_pressed(KeyCode.W):
            self.image = self.image_list[0]
            self.y += self.speed
        elif window.is_key_pressed(KeyCode.A):
            self.image = self.image_list[1]
            self.x -= self.speed
        elif window.is_key_pressed(KeyCode.S):
            self.image = self.image_list[3]
            self.y -= self.speed
        elif window.is_key_pressed(KeyCode.D):
            self.image = self.image_list[2]
            self.x += self.speed
        else:
            self.image = self.image_list[3]
            0
        if self.is_touching_any_sprite_with_tag("maze"):
            self.y = self.height / 2 + 20
            self.x = self.width / 2 + 20
        if self.is_touching_any_sprite_with_tag("dotattack"):
            score.score -= 1
        if score.score <= 0:
            window.delete_all_sprites()
    def on_left_click_anywhere(self):
        window.create_sprite(DuckAttack)

class Portal_IN(Sprite):
    def on_create(self):
        self.image = "img/portal.png"
        self.scale = 0.3
        self.add_tag("in")
        self.x = 56.5
        self.y = 58.5

class Water(Sprite):
    def on_create(self):
        self.image = "img/water.png"
        self.x = 889
        self.y = 307
        self.layer = 3
        self.scale = 0.25
        self.time = 0
        self.win = 0
    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag("duck"):
            self.time += dt
            if self.time > 1:
                window.delete_all_sprites()
                self.win += 1

class Bush(Sprite):
    def on_create(self):
        self.image = duck.image_list[4]
        self.scale = 0.7
        self.add_tag("maze")
        self.layer = 1


class Test(Sprite):
    def on_create(self):
        self.is_visible = False
    def on_left_click_anywhere(self):
        p = window.mouse_position
        msg = f"window.create_sprite(Bush, x={p.x}, y={p.y})"
        print(msg)


class DotTheEvil(Sprite):
    def on_create(self):
        self.image = dotimage[0]
        self.goto_random_position_in_region(217, self.height/2, window.width-self.width/2, window.height-self.height/2)
        self.scale = 0.4
        self.layer = 2
        self.t = 0
        self.it = 0
        self.health = 20
        self.add_tag("dot")
        self.dotattacktime = 0
        self.index = 0
        self.len = len(dotimage)
        self.rotation = 0 
        self.rotation_mode = RotationMode.RIGHT_LEFT
    def on_update(self, dt):
        self.move_forward(1)
        self.t += dt
        self.it += dt 
        self.dotattacktime += dt
        if self.t > 2:
            self.rotation += randint(0,90)
            self.t = 0
        if self.it > 0.25:
            self.index += 1
            self.image = dotimage[self.index % self.len]
            self.it = 0
        if self.dotattacktime > 1:
            attack = window.create_sprite(DotAttack)
            attack.position = self.position
            attack.point_toward_sprite(duck)
            self.dotattacktime = 0 
        if self.is_touching_any_sprite_with_tag("duckattack"):
            self.health -= 1
            if self.health <= 0:
                self.delete()


class DotAttack(Sprite):
    def on_create(self):
        self.speed = 2
        self.scale = 10
        self.color = Color.AMBER
        self.layer = 2
        self.t = 0
        self.add_tag("dotattack")
    def on_update(self, dt):
        self.move_forward(self.speed)
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_any_sprite_with_tag("duck"):
            self.t += dt
            if self.t > 2 * dt:
                self.delete()
        
class DuckAttack(Sprite):
    def on_create(self):
        self.speed = 3
        self.scale = 10
        self.color = Color.CYAN
        self.layer = 2
        self.t = 0
        self.add_tag("duckattack")
        self.position = duck.position
        self.point_toward_mouse_cursor()
        
    def on_update(self, dt):
        self.move_forward(self.speed)
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_any_sprite_with_tag("dot"):
            self.t += dt
            if self.t > 2 * dt:
                self.delete()

def level_1():
    window.create_sprite(Bush, x=223, y=602)
    window.create_sprite(Bush, x=223, y=545)
    window.create_sprite(Bush, x=224, y=458)
    window.create_sprite(Bush, x=224, y=370)
    window.create_sprite(Bush, x=203, y=107)
    window.create_sprite(Bush, x=208, y=19)
    window.create_sprite(Bush, x=511, y=399)
    window.create_sprite(Bush, x=622, y=405)
    window.create_sprite(Bush, x=683, y=408)
    window.create_sprite(Bush, x=733, y=404)
    window.create_sprite(Bush, x=822, y=412)
    window.create_sprite(Bush, x=909, y=415)
    window.create_sprite(Bush, x=968, y=408)
    window.create_sprite(Bush, x=1014, y=403)
    window.create_sprite(Bush, x=1009, y=351)
    window.create_sprite(Bush, x=1010, y=261)
    window.create_sprite(Bush, x=455, y=387)
    window.create_sprite(Bush, x=1010, y=202)
    window.create_sprite(Bush, x=1010, y=159)
    window.create_sprite(Bush, x=871, y=161)
    window.create_sprite(Bush, x=656, y=388)
    window.create_sprite(Bush, x=656, y=265)
    window.create_sprite(Bush, x=556, y=393)
    window.create_sprite(Bush, x=656, y=176)
    window.create_sprite(Bush, x=645, y=121)
    window.create_sprite(Bush, x=645, y=61)
    window.create_sprite(Bush, x=649, y=328)
    window.create_sprite(Bush, x=933, y=153)

# window.create_sprite(Test)

duck = window.create_sprite(Duck)
window.create_sprite(DotTheEvil)
score = window.create_label(Score)
window.create_sprite(Portal_IN)
water = window.create_sprite(Water)

level_1()


window.run()