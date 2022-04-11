from pycat.core import Window,Sprite,KeyCode

window = Window(enforce_window_limits=False)

class Ghost(Sprite):
    def on_create(self):
        self.image = "tiger.png"
        self.x = self.width/2
        self.y = 450
        self.opacity = 100
  
    def on_update(self,dt):
        if window.is_key_down(KeyCode.Z):
            self.x += 10
        if self.x >= 1155:
            print("Tigerrr WON")
            window.close()
        

class Elephant(Sprite):
    def on_create(self):
        self.image = "elephant.png"
        self.x = self.width/2
        print(self.x)
        self.y = 200

    def on_update(self, dt):
        if window.is_key_down(KeyCode.SLASH):
            self.x += 10
        if self.x >= 1155:
            print("Dumbo WON")
            window.close()
        

tigerrr = window.create_sprite(Ghost)

dumbo = window.create_sprite(Elephant)

window.run()