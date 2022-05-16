from pycat.core import Window,Sprite,KeyCode

window = Window()

class Owl(Sprite):
    def on_create(self):
        self.image = "img/owl.png"
        self.x = self.width/2
        self.y = window.height/2
        self.scale = 0.5
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
                print("owl is dead ;n;")


class Beach(Sprite):
    def on_create(self):
        self.image = "img/beach.png"
        self.scale = 0.5
        self.add_tag("b")

# class Ork(Sprite):
#     def on_create(self):
#         self.image = "img/ork1.png"
#     def on_update(self,dt):
#         self.point_toward(Owl.position)
#         self.move_forward(1)

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

b3 = window.create_sprite(Beach)
b3.height = 400
b3.width = 50
b3.y = window.height - b3.height/2
b3.x = 150

b4 = window.create_sprite(Beach)
b4.height = 400
b4.width = 50
b4.y = b4.height/2 + b1.height
b4.x = 300

b5 = window.create_sprite(Beach)
b5.height = 400
b5.width = 50
b5.y = window.height - b5.height/2
b5.x = 450


window.create_sprite(Owl)
# window.create_sprite(Ork)
        
window.run()
