from pycat.core import Window, Sprite, KeyCode, Color
from pycat.experimental import DraggableSprite
from pycat.base.event import KeyEvent
w = Window()
info_label = w.create_label()


class TestSprite(DraggableSprite):
    
    def on_create(self):
        self.scale_x = 100
        self.scale_y = 50
        self.position = w.center
        self.color = Color.WHITE
    
    def on_update(self, dt):
        if self is DraggableSprite.currently_dragged:
            if w.is_key_pressed(KeyCode.W):
                self.scale_y += 3
            if w.is_key_pressed(KeyCode.S):
                self.scale_y -= 3
            if w.is_key_pressed(KeyCode.A):
                self.scale_x -= 3
            if w.is_key_pressed(KeyCode.D):
                self.scale_x += 3
            
    
    def on_left_click(self):
        info_label.text = f"{self.position}, {self.scale_x}, {self.scale_y}"


def on_key_press(key: KeyEvent):
    if key.symbol == KeyCode.ENTER:
        w.create_sprite(TestSprite)

w.create_sprite(TestSprite)
w.run(on_key_press=on_key_press)
