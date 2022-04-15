from pycat.extensions import Turtle
from pycat.core import Window
from math import pi

window = Window()

turtle = window.create_sprite(Turtle)

def create_bubble(x, y, scale):
    r = (3600 * scale)/(2*pi)
    turtle.x = x
    turtle.y = y + r
    create_circle(scale)
    turtle.y -= 0.25*r
    turtle.x += 0.1*r
    create_circle(0.1*scale)

def create_circle(scale):
    for _ in range(3600):
        turtle.move_forward(scale)
        turtle.rotation -= 0.1
        

create_bubble(window.center.x,window.center.y,0.5)


        

# for i in range(345):
#     create_star(20)
#     turtle.goto_random_position()
#     turtle.rotation += 30
#     turtle.set_random_color()
#     turtle.pen_color = turtle.color




window.run()