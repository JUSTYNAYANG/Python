from pycat.core import Window, Sprite

window = Window()

class Ele(Sprite):
    def on_create(self):
        self.image = "elephant.png"
        self.goto_random_position()


for _ in range(100):
    window.create_sprite(Ele)
    

class Ghost(Sprite):
    def on_create(self):
        self.image = 'tiger.png'
        self.goto_random_position()
        self.opacity = 150
        self.layer = 1

ghost_tiger = window.create_sprite (Ghost)
ghost_tiger.y = 2.654332



for _ in range(50):
    window.create_sprite(Ghost)

print(type(ghost_tiger.image))
print(type(ghost_tiger.x))
print(type(ghost_tiger.y))
print(type(ghost_tiger.goto_random_position))
print(type(ghost_tiger.is_deleted))


window.run()
