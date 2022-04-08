from pycat.core import Window, Sprite

window = Window()

class Ghost(Sprite):
    def on_create(self):
        self.image = 'tiger.png'
        self.goto_random_position()
        self.opacity = 150
        self.layer = 1

ghost_tiger1 = window.create_sprite (Ghost)
ghost_tiger1.scale = 3
ghost_tiger1.x = ghost_tiger1.width/2
ghost_tiger1.y = window.height - ghost_tiger1.height/2

ghost_tiger2 = window.create_sprite (Ghost)
ghost_tiger2.x = 125
ghost_tiger2.y = 73.5

ghost_tiger3 = window.create_sprite (Ghost)
ghost_tiger3.x = 1280-125
ghost_tiger3.y = 640-73.5

ghost_tiger4 = window.create_sprite (Ghost)
ghost_tiger4.x = 1280-125
ghost_tiger4.y = 73.5



# print(window.width)
# print(window.height)
# print(ghost_tiger.width)
# print(ghost_tiger.height)

print(640-73.5)
print(147/2)

window.run()

