from UI import app_window
from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton
import json






class Room_window(app_window.window):
    def __init__(self) -> None:
        super().__init__()

        self.room_3d_frame = Entity(
            parent=self.win,
            color=color.white,
            world_scale=8,
            position = (-0.25, 0.2)
        )
        
        self.room_3d = Entity(
            parent=self.room_3d_frame,
            model='src/models/restaurant_mood',
            texture='src/models/restaurant_mood.png',
            scale=0.005,
            z=-10,
            rotation_x=20, 
            rotation_y=230,
            rotation_z=-20, 
        )

        self.submit = Button(
                        parent=self.win,
                        model="quad",
                        texture="src/icon/submit_button.png",
                        z=-15,
                        world_scale=2,
                        x=0.3,
                        y=-0.3,
                        highlighted_color=None,
                        on_click=lambda: print("test")
        )

    

    def slide_option(self):
        