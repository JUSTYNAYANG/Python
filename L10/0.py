from pycat.core import Window, Sprite, RotationMode

window = Window()
UP = 1
DOWN = 2
NOTICE = 3
SCARED = 4
RUN1 = 5
RUN2 = 6
DINO = 7



class Blob(Sprite):
    def on_create(self):
        self.x = window.width*3/4
        self.y = 350
        self.image = "img/ghost-a.png"
        self.state = UP
        self.extra = 8
        self.t = 0
        # self.t2 = 0
        self.ud = 0
        # self.d = 0
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.rotation = 90
    def on_update(self, dt):
        self.t += dt
        # self.t2 += dt
        if self.state == UP:
            self.blobup()
        elif self.state == DOWN:
            self.blobdown()
        elif self.state == NOTICE:
            self.blobnotice()
        elif self.state == SCARED:
            self.blobscared()
        elif self.state == RUN1:
            self.blobrun1()
        elif self.state == RUN2:
            self.blobrun2()
        if self.state == DINO:
             self.dino()
    
    def blobup(self):
        self.image = "img/ghost-a.png"
        self.move_forward(2.5)
        self.rotation = 90
        if self.y > 350:
            self.state = DOWN
    def blobdown(self):
        self.move_forward(2.5)
        self.rotation = -90
        if self.ud < 4:
            if self.y < 250:
                self.ud += 1
                # self.d += 1
                self.state = UP
        else:
            self.t = 0
            self.state = DINO 
        # if self.d == 4:
        #     self.t2 = 0
        #     self.extra = DINO
    def dino(self):
        window.create_sprite(Dino)
        self.state = NOTICE
    def blobnotice(self):
        self.image = "img/ghost-b.png"
        self.ud = 0
        if self.t > 2:
            self.t = 0
            self.state = SCARED
    def blobscared(self):
        self.image = "img/ghost-c.png"
        if self.t > 2:
            self.t = 0
            self.state = RUN1
    def blobrun1(self):
        self.image = "img/ghost-d.png"
        self.rotation = 0
        self.move_forward(2)
        if self.is_touching_window_edge():
            self.is_visible = False
            self.x -= window.width
            self.state = RUN2
    def blobrun2(self):
        self.is_visible = True
        if self.x < window.width*2/3:
             self.x += 2
        else:
            self.state = UP
    

class Dino(Sprite):
    def on_create(self):
        self.x = window.width/3
        self.y = window.height/2
        self.image = "img/dinosaur4-d.png" 
    def on_update(self, dt):
        if blob.t >= 2:
            self.delete()
# should make self . time follow blob.t


blob = window.create_sprite(Blob)
window.run()