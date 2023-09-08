from UI import app_window
from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton
import json


with open("game/data/player_info.json", "r") as db_file:
    Info = json.load(db_file)

try:
    ROOM = [i for i in scene.entities if i.name == "room"][0]
except IndexError:
    ROOM = None


class Room_window(app_window.window):
    def __init__(self) -> None:
        super().__init__()
        with open("game/data/player_info.json", "r") as db_file:
            Info = json.load(db_file)
        self.room = Info["room"]

        self.room_3d_frame = Entity(
            parent=self.win,
            #model="quad",
            world_scale=7,
            position = (-0.25, 0.1),
        )
        
        self.room_3d = Entity(
            parent=self.room_3d_frame,
            model=f'src/models/restaurant_{self.room}',
            texture=f'src/models/restaurant_{self.room}.png',
            scale=0.005,
            z=-10,
            y=0.2,
            rotation_x=20, 
            rotation_y=230,
            rotation_z=-20, 
            origin = (-60, 3, 60),
            update = self.animation_rotate_room
        )
        self.test_origin = Entity(
            parent=self.room_3d,
            model="sphere",
            color = color.red
        )

        self.submit = Entity(
                        parent=self.win,
                        model="quad",
                        texture="src/icon/submit_button.png",
                        z=-15,
                        world_scale=2,
                        x=0.3,
                        y=-0.3,
                        collider='box',
                        on_click=lambda: print("test")
        )

        

        self.money_up = slide_option(self.win, "money", "src/icon/coin.png", (-0.4, 0), Info["up"]["money"])
        self.clean_up = slide_option(self.win, "clean", "src/icon/clean.png", (-0.3, 0), Info["up"]["clean"])
        self.taste_up = slide_option(self.win, "taste", "src/icon/taste.png", (-0.2, 0), Info["up"]["taste"])
        self.ads_up = slide_option(self.win, "ads", "src/icon/youtube.png", (-0.1, 0), Info["up"]["ads"])

        self.room_mood = room_select(self.win, "mood", (0.05, 0.2, -12))
        self.room_pop = room_select(self.win, "pop", (0.2, 0.2, -12))
        self.room_pop = room_select(self.win, "brick", (0.35, 0.2, -12))




    def animation_rotate_room(self):
        self.room_3d.rotation_y  = mouse.position.x*-100 + 230
        pass


    

class room_select(Button):
    def __init__(self, window, name:str, position:Vec2) -> None:
        super().__init__(
            parent=window,
            model="quad",
            texture="/../sources/item_frame.png",
            world_scale=3,
            color=color.dark_gray,
            position=position
        )
        self.object = Entity(
            parent=self,
            model=f'src/models/restaurant_{name}',
            texture=f'src/models/restaurant_{name}.png',
            scale=0.005,
            rotation_x=20, 
            rotation_y=230,
            rotation_z=-20, 
            origin = (-60, 3, 60),
            update=self.object_animation
        )
        self.checked = Sprite(
            parent=self,
            texture="src/icon/check.png",
            scale=0.1,
            position=(0, 0, -1),
            visible=Info["room"] == name
        )
        self.buy = Button(
            parent=self,
            model="quad",
            text="10000$",
            world_scale_x=2,
            world_scale_y=0.5,
            color=color.green,
            position=(0, 0, -1),
            visible=False,
            enable=False,
        )

        self.name = name
        if Info["room"] == name:
            self.highlight_color = self.color
            self.pressed_color = self.color

    def object_animation(self):
        self.object.rotation_y  = mouse.position.x*-100 + 230
    
    def on_click(self):
        if Info["room"] == self.name:
            return None
        self.buy.visible = True
        self.buy.enable = True
        self.buy.on_click=self.is_buy
    
    def is_buy(self):
        global ROOM
        Info["room"] = self.name
        with open("game/data/player_info.json", "w") as db_file:
            json.dump(Info, db_file, indent=1)
        app_window.window().invisibled()

        while True:
            if ROOM is not None:
                ROOM.visible=False
                ROOM.enabled = False
                ROOM.disable()
                ROOM = Entity(name="room", model=f'src/models/restaurant_{Info["room"]}', texture=f'src/models/restaurant_{Info["room"]}.png', rotation_y=180, scale=0.24)
                break
            else:
                try:
                    ROOM = [i for i in scene.entities if i.name == "room"][0]
                except IndexError:
                    ROOM = None
    







class slide_option:
    def __init__(self, window, name, icon_path:Path, position:Vec2, default_value:float = 1/4 * 500, option:str="up"):
        self.option=option
        self.name = name
        Info = {}
        self.slider_container = Entity(
            #model="quad",
            #color=color.white,
            parent=window,
            world_scale_x=0.2,
            world_scale_y=5,
            position=position,
            z=-20
        )
        self.slider = Slider(
            parent=self.slider_container,
            min=0,
            max=500,
            world_scale_x=0.2,
            world_scale_y=400,
            vertical=True,
            y=-0.5,
            default=default_value,
        )
        if self.option == "up":
            self.slider.on_value_changed = self.slider_changed

        self.slider.knob.model="quad"
        self.slider.knob.world_scale_x=0.25
        self.slider.knob.world_scale_y=0.5
        slider_icon = Entity(
            parent=self.slider_container,
            model="quad",
            texture=icon_path,
            y=-0.65,
            world_scale=0.75,
        )

        
    
    def slider_changed(self):
        ups = Info[self.option]
        Info[self.option][self.name] = self.slider.value
        value_sum = sum(list(map(lambda a: ups[a], list(ups)))) - 1000

        # print("value: "+ str(self.slider.value))
        # print("more: "+ str(value_sum))
        # print("sum: "+ str(sum(list(map(lambda a: ups[a], list(ups))))))
        # print("minus: " + str(self.slider.value - value_sum))

        if value_sum > 0:
            self.slider.value -= value_sum

        #save
        Info[self.option][self.name] = self.slider.value
        with open("game/data/player_info.json", "w") as db_file:
            json.dump(Info, db_file, indent=1)
        