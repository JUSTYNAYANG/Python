from pycat.core import Window, Sprite, KeyCode
window = Window()

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
        print(self.width)
        print(self.height)
        print(window.height)
        print(window.width)
        print(window.width/self.width)
        print(window.height/self.height)



duck = window.create_sprite(Duck)
window.create_sprite(Bush)

window.run()