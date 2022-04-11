from pycat.core import Window

window = Window()

e = window.create_sprite()

e.image = 'elephant.png'

e.goto_random_position()

t = window.create_sprite()
t.image = 'tiger.png'

t.x = 800
t.y = 200

m = "elephant properties: (x,y) = "+"("+str(e.x)+","+str(e.y)+")"
print(m)

window.run()
