from pycat.extensions import Turtle
from pycat.core import Window

window = Window()

turtle = window.create_sprite(Turtle, position= window.center)


def create_star(scale):
    for _ in range(5):
        turtle.move_forward(scale)
        turtle.rotation -= 720/5
        

for i in range(345):
    create_star(20)
    turtle.goto_random_position()
    turtle.rotation += 30
    turtle.set_random_color()
    turtle.pen_color = turtle.color




window.run()