from pycat.core import Window

window = Window()

elephant = window.create_sprite()

elephant.image = 'elephant.png'
elephant.x = 200
elephant.y = 200

elephant.goto_random_position()

tiger = window.create_sprite()
tiger.image = 'tiger.png'

tiger.x = 800
tiger.y = 200

window.run()

