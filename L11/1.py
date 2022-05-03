from pycat.core import Window, Sprite, Color
window = Window()

image = ["img/1.jpg", "img/2.jpg", "img/3.jpg", "img/4.jpg", "img/5.jpg", "img/6.jpg", "img/7.jpg", "img/8.jpg", "img/9.jpg", "img/10.jpg"]
window.background_image = image[0]
    
class Next(Sprite):
    def on_create(self):
        self.scale = 100
        self.x = window.width/2
        self.y = self.height
        self.color = Color(0, 102, 102)
        self.index = 1
        self.len = len(image)
    def on_left_click(self):
        # if self.index < 2:
        #     self.index += 1
        # else:
        #     self.index = 0
        # window.background_image = image[self.index]

        self.index += 1
        window.background_image = image[self.index % self.len]


window.create_sprite(Next)
window.run()