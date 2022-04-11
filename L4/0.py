from pycat.core import Window,Sprite,KeyCode

window = Window()

class Owl(Sprite):
    def on_create(self):
        self.image = "img/owl.png"
        self.x = self.width
        self.y = window.height/2
        self.health = 100
    
    def on_update(self,dt):
        self.move_forward(1)
        if window.is_key_down(KeyCode.D):
            self.rotation = 0
        if window.is_key_down(KeyCode.W):
            self.rotation = 90
        if window.is_key_down(KeyCode.A):
            self.rotation = 180
        if window.is_key_down(KeyCode.S):
            self.rotation = 270
        if self.is_touching_any_sprite_with_tag("b"):
            print("ouch")
            self.health -= 0.5
            print(self.health)
            if self.health <= 0:
                window.close()


class Beach(Sprite):
    def on_create(self):
        self.image = "img/beach.png"
        self.add_tag("b")

b1 = window.create_sprite(Beach)
b1.height /= 2
b1.width = 640
b1.y = b1.height/2
b1.x = b1.width/2

b2 = window.create_sprite(Beach)
b2.height /= 2
b2.width = 420
b2.y = b2.height/2
b2.x = window.width - b2.width/2

window.create_sprite(Owl)
        
window.run()