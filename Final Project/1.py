from pycat.core import Window, Sprite, KeyCode
from pycat.experimental.simple_level_editor import start_level_editor
from level import generate_level

window = Window()

# bush width 112.2
# bush height 85.2
# window width 1280
# window height 640
# window width / bush width (around how many bush can fit horizontally) 11.408199643493761
# window height / bush height (around how many bush can fit vertically)7.511737089201878

class Duck(Sprite):
    def on_create(self):
        self.image_list = ["img/duck 1.png", "img/duck 2.png", "img/duck 3.png", "img/duck 4.png", "img/Tree1.png"]
        self.image = self.image_list[0]
        self.state = 0
        self.y = self.height / 2 + 20
        self.x = self.width / 2 + 20
        self.speed = 2
        self.scale = 0.7
        self.layer = 1

    def on_update(self,dt):
        if window.is_key_pressed(KeyCode.W):
            self.image = self.image_list[0]
            self.y += self.speed
        elif window.is_key_pressed(KeyCode.A):
            self.image = self.image_list[1]
            self.x -= self.speed
        elif window.is_key_pressed(KeyCode.S):
            self.image = self.image_list[3]
            self.y -= self.speed
        elif window.is_key_pressed(KeyCode.D):
            self.image = self.image_list[2]
            self.x += self.speed
        else:
            self.image = self.image_list[3]
            0
        if self.is_touching_any_sprite_with_tag("maze"):
            self.y = self.height / 2 + 20
            self.x = self.width / 2 + 20
class Bush(Sprite):
    def on_create(self):
        self.image = duck.image_list[4]
        self.scale = 0.3
        self.add_tag("maze")
        self.layer = 1


class Test(Sprite):
    def on_create(self):
        self.is_visible = False
    def on_left_click_anywhere(self):
        p = window.mouse_position
        msg = f"window.create_sprite(Bush, x={p.x}, y={p.y})"
        print(msg)

window.create_sprite(Test)

duck = window.create_sprite(Duck)
window.create_sprite(Bush, x=0, y=152)
window.create_sprite(Bush, x=38, y=150)
window.create_sprite(Bush, x=76, y=150)
window.create_sprite(Bush, x=112, y=150)
window.create_sprite(Bush, x=150, y=152)
window.create_sprite(Bush, x=126, y=42)
window.create_sprite(Bush, x=126, y=18)
window.create_sprite(Bush, x=70, y=262)
window.create_sprite(Bush, x=72, y=300)
window.create_sprite(Bush, x=68, y=326)
window.create_sprite(Bush, x=68, y=360)
window.create_sprite(Bush, x=66, y=396)
window.create_sprite(Bush, x=68, y=428)
window.create_sprite(Bush, x=72, y=460)
window.create_sprite(Bush, x=60, y=482)
window.create_sprite(Bush, x=564, y=145)
window.create_sprite(Bush, x=602, y=141)
window.create_sprite(Bush, x=643, y=141)
window.create_sprite(Bush, x=689, y=142)
window.create_sprite(Bush, x=728, y=142)
window.create_sprite(Bush, x=774, y=145)
window.create_sprite(Bush, x=831, y=143)
window.create_sprite(Bush, x=890, y=147)
window.create_sprite(Bush, x=942, y=142)
window.create_sprite(Bush, x=797, y=145)
window.create_sprite(Bush, x=867, y=138)
window.create_sprite(Bush, x=914, y=146)
window.create_sprite(Bush, x=937, y=177)
window.create_sprite(Bush, x=521, y=142)
window.create_sprite(Bush, x=934, y=240)
window.create_sprite(Bush, x=544, y=182)
window.create_sprite(Bush, x=537, y=219)
window.create_sprite(Bush, x=549, y=256)
window.create_sprite(Bush, x=585, y=262)
window.create_sprite(Bush, x=637, y=259)
window.create_sprite(Bush, x=752, y=251)
window.create_sprite(Bush, x=800, y=251)
window.create_sprite(Bush, x=933, y=210)
window.create_sprite(Bush, x=826, y=250)
window.create_sprite(Bush, x=711, y=251)
window.create_sprite(Bush, x=683, y=257)
window.create_sprite(Bush, x=527, y=248)
window.create_sprite(Bush, x=749, y=130)
window.create_sprite(Bush, x=749, y=107)
window.create_sprite(Bush, x=756, y=72)
window.create_sprite(Bush, x=1046, y=236)
window.create_sprite(Bush, x=1047, y=209)
window.create_sprite(Bush, x=1048, y=185)
window.create_sprite(Bush, x=1102, y=175)
window.create_sprite(Bush, x=1143, y=179)
window.create_sprite(Bush, x=1154, y=213)
window.create_sprite(Bush, x=1159, y=277)
window.create_sprite(Bush, x=1157, y=307)
window.create_sprite(Bush, x=1179, y=312)
window.create_sprite(Bush, x=1205, y=308)
window.create_sprite(Bush, x=1204, y=263)
window.create_sprite(Bush, x=1199, y=228)
window.create_sprite(Bush, x=1179, y=262)
window.create_sprite(Bush, x=1153, y=359)
window.create_sprite(Bush, x=1202, y=290)
window.create_sprite(Bush, x=1158, y=245)
window.create_sprite(Bush, x=1156, y=335)
window.create_sprite(Bush, x=607, y=259)
window.create_sprite(Bush, x=781, y=258)
window.create_sprite(Bush, x=662, y=248)
window.create_sprite(Bush, x=537, y=163)
window.create_sprite(Bush, x=260, y=54)
window.create_sprite(Bush, x=283, y=54)
window.create_sprite(Bush, x=302, y=57)
window.create_sprite(Bush, x=331, y=58)
window.create_sprite(Bush, x=350, y=57)
window.create_sprite(Bush, x=85, y=349)
window.create_sprite(Bush, x=99, y=347)
window.create_sprite(Bush, x=386, y=59)
window.create_sprite(Bush, x=135, y=347)
window.create_sprite(Bush, x=152, y=345)
window.create_sprite(Bush, x=175, y=433)
window.create_sprite(Bush, x=197, y=435)
window.create_sprite(Bush, x=229, y=434)
window.create_sprite(Bush, x=253, y=472)
window.create_sprite(Bush, x=249, y=455)
window.create_sprite(Bush, x=256, y=425)
window.create_sprite(Bush, x=255, y=402)
window.create_sprite(Bush, x=252, y=349)
window.create_sprite(Bush, x=253, y=306)
window.create_sprite(Bush, x=253, y=264)
window.create_sprite(Bush, x=253, y=191)
window.create_sprite(Bush, x=250, y=161)
window.create_sprite(Bush, x=163, y=265)
window.create_sprite(Bush, x=178, y=265)
window.create_sprite(Bush, x=200, y=266)
window.create_sprite(Bush, x=232, y=267)
window.create_sprite(Bush, x=76, y=576)
window.create_sprite(Bush, x=103, y=573)
window.create_sprite(Bush, x=165, y=580)
window.create_sprite(Bush, x=189, y=585)
window.create_sprite(Bush, x=211, y=602)
window.create_sprite(Bush, x=220, y=631)
window.create_sprite(Bush, x=222, y=639)
window.create_sprite(Bush, x=366, y=633)
window.create_sprite(Bush, x=397, y=564)
window.create_sprite(Bush, x=386, y=511)
window.create_sprite(Bush, x=385, y=508)
window.create_sprite(Bush, x=527, y=563)
window.create_sprite(Bush, x=555, y=547)
window.create_sprite(Bush, x=533, y=481)
window.create_sprite(Bush, x=527, y=458)
window.create_sprite(Bush, x=531, y=432)
window.create_sprite(Bush, x=531, y=412)
window.create_sprite(Bush, x=690, y=638)
window.create_sprite(Bush, x=693, y=622)
window.create_sprite(Bush, x=689, y=600)
window.create_sprite(Bush, x=690, y=532)
window.create_sprite(Bush, x=698, y=512)
window.create_sprite(Bush, x=712, y=599)
window.create_sprite(Bush, x=863, y=486)
window.create_sprite(Bush, x=864, y=432)
window.create_sprite(Bush, x=871, y=508)
window.create_sprite(Bush, x=917, y=516)
window.create_sprite(Bush, x=1011, y=516)
window.create_sprite(Bush, x=1075, y=502)
window.create_sprite(Bush, x=969, y=599)
window.create_sprite(Bush, x=967, y=540)
window.create_sprite(Bush, x=967, y=532)
window.create_sprite(Bush, x=1164, y=637)
window.create_sprite(Bush, x=1164, y=601)
window.create_sprite(Bush, x=1164, y=582)
window.create_sprite(Bush, x=1163, y=474)
window.create_sprite(Bush, x=1233, y=484)
window.create_sprite(Bush, x=250, y=381)
window.create_sprite(Bush, x=254, y=328)
window.create_sprite(Bush, x=250, y=285)
window.create_sprite(Bush, x=247, y=493)
window.create_sprite(Bush, x=242, y=245)
window.create_sprite(Bush, x=254, y=221)
window.create_sprite(Bush, x=252, y=139)
window.create_sprite(Bush, x=521, y=537)
window.create_sprite(Bush, x=540, y=511)
window.create_sprite(Bush, x=562, y=531)
window.create_sprite(Bush, x=560, y=471)
window.create_sprite(Bush, x=559, y=410)
window.create_sprite(Bush, x=554, y=569)
window.create_sprite(Bush, x=677, y=572)
window.create_sprite(Bush, x=701, y=572)
window.create_sprite(Bush, x=718, y=563)
window.create_sprite(Bush, x=724, y=523)
window.create_sprite(Bush, x=675, y=498)
window.create_sprite(Bush, x=719, y=633)
window.create_sprite(Bush, x=235, y=577)
window.create_sprite(Bush, x=122, y=574)
window.create_sprite(Bush, x=854, y=467)
window.create_sprite(Bush, x=852, y=390)
window.create_sprite(Bush, x=948, y=512)
window.create_sprite(Bush, x=985, y=504)
window.create_sprite(Bush, x=1044, y=516)
window.create_sprite(Bush, x=961, y=576)
window.create_sprite(Bush, x=966, y=625)
window.create_sprite(Bush, x=1196, y=473)
window.create_sprite(Bush, x=1265, y=476)
window.create_sprite(Bush, x=1076, y=182)
window.create_sprite(Bush, x=567, y=501)
window.create_sprite(Bush, x=564, y=436)
window.create_sprite(Bush, x=239, y=608)
window.create_sprite(Bush, x=399, y=624)
window.create_sprite(Bush, x=393, y=605)
window.create_sprite(Bush, x=373, y=604)
window.create_sprite(Bush, x=371, y=582)
window.create_sprite(Bush, x=370, y=560)
window.create_sprite(Bush, x=359, y=530)
window.create_sprite(Bush, x=403, y=540)
window.create_sprite(Bush, x=1265, y=106)
window.create_sprite(Bush, x=1269, y=91)
window.create_sprite(Bush, x=1269, y=68)
window.create_sprite(Bush, x=1268, y=39)
window.create_sprite(Bush, x=1268, y=15)
window.create_sprite(Bush, x=1093, y=156)
window.create_sprite(Bush, x=1100, y=128)
window.create_sprite(Bush, x=1097, y=107)
window.create_sprite(Bush, x=1095, y=90)
window.create_sprite(Bush, x=1117, y=85)
window.create_sprite(Bush, x=1120, y=102)
window.create_sprite(Bush, x=1115, y=127)
window.create_sprite(Bush, x=1125, y=161)
window.create_sprite(Bush, x=611, y=26)
window.create_sprite(Bush, x=615, y=8)
window.create_sprite(Bush, x=911, y=29)
window.create_sprite(Bush, x=909, y=11)
window.create_sprite(Bush, x=375, y=84)
window.create_sprite(Bush, x=363, y=105)
window.create_sprite(Bush, x=364, y=124)
window.create_sprite(Bush, x=368, y=146)
window.create_sprite(Bush, x=362, y=169)
window.create_sprite(Bush, x=363, y=200)
window.create_sprite(Bush, x=363, y=230)
window.create_sprite(Bush, x=363, y=253)
window.create_sprite(Bush, x=365, y=269)
window.create_sprite(Bush, x=361, y=300)
window.create_sprite(Bush, x=359, y=327)
window.create_sprite(Bush, x=358, y=345)
window.create_sprite(Bush, x=355, y=387)
window.create_sprite(Bush, x=394, y=378)
window.create_sprite(Bush, x=449, y=376)
window.create_sprite(Bush, x=512, y=374)
window.create_sprite(Bush, x=520, y=374)
window.create_sprite(Bush, x=672, y=367)
window.create_sprite(Bush, x=727, y=368)
window.create_sprite(Bush, x=823, y=378)
window.create_sprite(Bush, x=918, y=370)
window.create_sprite(Bush, x=983, y=365)
window.create_sprite(Bush, x=1009, y=365)
window.create_sprite(Bush, x=1079, y=365)
window.create_sprite(Bush, x=1121, y=366)
window.create_sprite(Bush, x=877, y=414)
window.create_sprite(Bush, x=354, y=371)
window.create_sprite(Bush, x=419, y=379)
window.create_sprite(Bush, x=478, y=374)
window.create_sprite(Bush, x=545, y=371)
window.create_sprite(Bush, x=583, y=375)
window.create_sprite(Bush, x=623, y=369)
window.create_sprite(Bush, x=643, y=370)
window.create_sprite(Bush, x=700, y=379)
window.create_sprite(Bush, x=766, y=380)
window.create_sprite(Bush, x=799, y=380)
window.create_sprite(Bush, x=862, y=379)
window.create_sprite(Bush, x=885, y=384)
window.create_sprite(Bush, x=934, y=384)
window.create_sprite(Bush, x=949, y=357)
window.create_sprite(Bush, x=1045, y=368)

window.run()