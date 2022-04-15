from pycat.extensions import Turtle
from pycat.core import Window

window = Window()

turtle = window.create_sprite(Turtle, position= window.center)


def create_square():
    for _ in range(4):
        turtle.move_forward(100)
        turtle.rotation -= 90

for _ in range(36):
    create_square()
    turtle.rotation += 10




window.run()