from pycat.core import Window

animal = input("ANIMAL ")
positionx = int(input("X "))


window = Window()

chosen_animal = window.create_sprite()
chosen_animal.x = positionx

if animal == "elephant":
    chosen_animal.image = 'elephant.png'
elif animal == "tiger":
    chosen_animal.image = "tiger.png"
    




window.run()

