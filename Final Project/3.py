from pycat.core import Window, Sprite, KeyCode, RotationMode, Color, Label
from random import randint
from pycat.experimental.simple_level_editor import start_level_editor
from level import generate_level

window = Window()
# start_level_editor(window, "Final Project/eheh.py")
# generate_level(window, "Final Project/eheh.py")
dotimage = ["img/dot-b.png", "img/dot-c.png"]
portal_in_x = [56.5, 82, 47]
portal_in_y = [58.5, 99, 597]
portal_out_x = [889, 1221, 651]
portal_out_y =[307, 125, 411]
class Score(Label):
    def on_create(self):
        self.text = "100"
        self.score = 100
        self.t = 0
        self.level = 0
    def on_update(self, dt):
        self.text = str(int(self.score))
        if self.score <= 0:
            self.text = "                      YOU DIED......\n\n NO the DUCK DIED and it's YOUR FAULT"
            self.y = window.height/2
            self.x = window.width/2 - 300
            self.t += dt
            if self.t >= 10:
                window.close()
        if duck.win == 1:
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
        self.speed = 3
        self.scale = 0.7
        self.layer = 1
        self.win = 0
        self.time = 0
        self.add_tag("duck")
        self.status = 0
        self.state = 0

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
            score.score -= 2
        if score.score <= 0:
            window.delete_all_sprites()
        if self.is_touching_any_sprite_with_tag("water"):
            self.time += dt
            if self.time > 1:
                window.delete_all_sprites()
                self.win += 1
        if self.is_touching_any_sprite_with_tag("out"):
            self.status += dt
            if self.status > 1:
                self.is_visible = False
                self.state += 1
                self.status = 0
    def on_left_click_anywhere(self):
        window.create_sprite(DuckAttack)

class Portal_IN(Sprite):
    def on_create(self):
        self.image = "img/portal.png"
        self.scale = 0.3
        self.add_tag("in")
        self.x = portal_in_x[score.level]
        self.y = portal_in_y[score.level]

class Portal_OUT(Sprite):
    def on_create(self):
        self.image = "img/portal.png"
        self.scale = 0.3
        self.add_tag("out")
        self.x = portal_out_x[score.level]
        self.y = portal_out_y[score.level]

class Water(Sprite):
    def on_create(self):
        self.image = "img/water.png"
        self.x = portal_out_x[2]
        self.y = portal_out_y[2]
        self.layer = 3
        self.scale = 0.25
        self.add_tag("water")


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
        self.layer = 3
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
    window.create_sprite(DotTheEvil)
    window.create_sprite(Portal_IN)
    window.create_sprite(Portal_OUT)
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

def level_2():
    window.create_sprite(DotTheEvil)
    window.create_sprite(DotTheEvil)
    window.create_sprite(Portal_IN)
    window.create_sprite(Portal_OUT)
    window.create_sprite(Bush, x=168, y=343)
    window.create_sprite(Bush, x=179, y=264)
    window.create_sprite(Bush, x=436, y=441)
    window.create_sprite(Bush, x=419, y=311)
    window.create_sprite(Bush, x=425, y=215)
    window.create_sprite(Bush, x=428, y=87)
    window.create_sprite(Bush, x=665, y=447)
    window.create_sprite(Bush, x=677, y=323)
    window.create_sprite(Bush, x=675, y=244)
    window.create_sprite(Bush, x=663, y=196)
    window.create_sprite(Bush, x=688, y=316)
    window.create_sprite(Bush, x=735, y=316)
    window.create_sprite(Bush, x=850, y=302)
    window.create_sprite(Bush, x=905, y=494)
    window.create_sprite(Bush, x=895, y=592)
    window.create_sprite(Bush, x=899, y=625)
    window.create_sprite(Bush, x=1044, y=301)
    window.create_sprite(Bush, x=1089, y=325)
    window.create_sprite(Bush, x=1267, y=321)
    window.create_sprite(Bush, x=1068, y=14)
    window.create_sprite(Bush, x=179, y=603)
    window.create_sprite(Bush, x=179, y=555)
    window.create_sprite(Bush, x=182, y=485)
    window.create_sprite(Bush, x=178, y=413)
    window.create_sprite(Bush, x=424, y=376)
    window.create_sprite(Bush, x=412, y=270)
    window.create_sprite(Bush, x=419, y=148)
    window.create_sprite(Bush, x=680, y=394)
    window.create_sprite(Bush, x=883, y=551)
    window.create_sprite(Bush, x=785, y=301)
    window.create_sprite(Bush, x=1159, y=324)
    window.create_sprite(Bush, x=1210, y=321)

def level_3():
    window.create_sprite(DotTheEvil)
    window.create_sprite(DotTheEvil)
    window.create_sprite(DotTheEvil)
    window.create_sprite(Portal_IN)
    window.create_sprite(Water)
    window.create_sprite(Bush, x=211, y=575)
    window.create_sprite(Bush, x=185, y=519)
    window.create_sprite(Bush, x=963, y=529)
    window.create_sprite(Bush, x=510, y=494)
    window.create_sprite(Bush, x=513, y=441)
    window.create_sprite(Bush, x=514, y=330)
    window.create_sprite(Bush, x=510, y=276)
    window.create_sprite(Bush, x=534, y=144)
    window.create_sprite(Bush, x=533, y=111)
    window.create_sprite(Bush, x=588, y=151)
    window.create_sprite(Bush, x=725, y=127)
    window.create_sprite(Bush, x=803, y=126)
    window.create_sprite(Bush, x=520, y=386)
    window.create_sprite(Bush, x=514, y=215)
    window.create_sprite(Bush, x=655, y=132)
    window.create_sprite(Bush, x=186, y=429)
    window.create_sprite(Bush, x=213, y=633)
    window.create_sprite(Bush, x=164, y=166)
    window.create_sprite(Bush, x=175, y=247)
    window.create_sprite(Bush, x=189, y=312)
    window.create_sprite(Bush, x=176, y=371)
    window.create_sprite(Bush, x=911, y=514)
    window.create_sprite(Bush, x=817, y=515)
    window.create_sprite(Bush, x=695, y=513)
    window.create_sprite(Bush, x=563, y=499)
    window.create_sprite(Bush, x=774, y=338)
    window.create_sprite(Bush, x=778, y=418)
    window.create_sprite(Bush, x=779, y=452)
    window.create_sprite(Bush, x=1031, y=283)
    window.create_sprite(Bush, x=1043, y=330)
    window.create_sprite(Bush, x=1029, y=426)
    window.create_sprite(Bush, x=1019, y=492)
    window.create_sprite(Bush, x=628, y=499)
    window.create_sprite(Bush, x=758, y=519)
    window.create_sprite(Bush, x=1043, y=380)

class Levels(Sprite):
    def on_create(self):
        self.is_visible = False
        self.repeat = 0
        level_1()
    def on_update(self, dt):
        if duck.state == 1:
            window.delete_sprites_with_tag("in")
            window.delete_sprites_with_tag("maze")
            window.delete_sprites_with_tag("out")
            window.delete_sprites_with_tag("dotattack")
            window.delete_sprites_with_tag("dot")
            window.delete_sprites_with_tag("duckattack")
            duck.state = 0
            score.level += 1
            self.repeat += 1
        if score.level == 1 and self.repeat == 1:
            level_2()
            self.repeat += 1
            duck.is_visible = True
            duck.x = portal_in_x[score.level]
            duck.y = portal_in_y[score.level]
        if score.level == 2 and self.repeat == 3:
            level_3()
            self.repeat += 1
            duck.is_visible = True
            duck.x = portal_in_x[score.level]
            duck.y = portal_in_y[score.level]

            

# window.create_sprite(Test)

duck = window.create_sprite(Duck)
score = window.create_label(Score)
# water = window.create_sprite(Water)
window.create_sprite(Levels)




window.run()