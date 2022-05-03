from pycat.core import Window, Sprite, Color
window = Window()

image = ["img/1.jpg", "img/2.jpg", "img/3.jpg"]
window.background_image = image[0]

class One(Sprite):
    def on_create(self):
        self.scale = 100
        self.x = window.width/4
        self.y = self.height
        self.color = Color.MAGENTA
    def on_left_click(self):
            window.background_image = image[0]

class Two(Sprite):
    def on_create(self):
        self.scale = 100
        self.x = window.width/2
        self.y = self.height
        self.color = Color(51, 102, 153)
    def on_left_click(self):
            window.background_image = image[1]
    
class Three(Sprite):
    def on_create(self):
        self.scale = 100
        self.x = window.width/4*3
        self.y = self.height
        self.color = Color(0, 102, 102)
    def on_left_click(self):
            window.background_image = image[2]

window.create_sprite(One)
window.create_sprite(Two)
window.create_sprite(Three)


window.run()