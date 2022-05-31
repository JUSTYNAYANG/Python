from pycat.core import Window, Sprite, KeyCode
window = Window()

# bush width 112.2
# bush height 85.2
# window width 1280
# window height 640
# window width / bush width (around how many bush can fit horizontally) 11.408199643493761
# window height / bush height (around how many bush can fit vertically)7.511737089201878

class Duck(Sprite):
    def on_create(self):
        self.image_list = ["img/duck 1.png", "img/duck 2.png", "img/duck 3.png", "img/duck 4.png", "img/Tree1.png"]
        self.image = self.image_list[0]
        self.state = 0
        self.y = self.height / 2 + 20
        self.x = self.width / 2 + 20
        self.speed = 2
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

class Bush(Sprite):
    def on_create(self):
        self.image = duck.image_list[4]
        self.scale = 0.6
        self.x = 300
        self.y = 300



duck = window.create_sprite(Duck)
window.create_sprite(Bush)

window.run()