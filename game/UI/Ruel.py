from UI import app_window, UI_tools
from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton
import json



RULE_ROWS=8
RULE_COLUMNS=3







class Rule_window(app_window.window):
    def __init__(self, rule_name=None) -> None:
        super().__init__()

        self.main_containers = Entity(
            name=self.win_name,
            parent=self.win,
            world_scale_x=20,
            world_scale_y=10,
            z=-4
        )
        for i in range(-4, 5):
            space = i/100
            self.option("test", (-0.35, i/10 + space))
            self.option("test", (0, i/10 + space))
            self.option("test", (0.35, i/10 + space))
        



    def option(self, name,  position:Vec2 = (-0.35, 0.4)):

        option_container = Entity(
            name= str(self.win_name) + ".container." + str(name),
            parent=self.main_containers,
            position=position,
            scale_x=0.3,
            scale_y=0.1,
            z=-5,
        )
        option = Text(
            name=str(self.win_name) + ".container." + str(name),
            parent=option_container,
            #color = color.white,
            world_scale=15,
            z=-6,
            text="can get laptop",
            color=color.white,
            x=-0.3
        )

        toogle = UI_tools.Switch(parent=option_container, position = (0.4, 0, -50), scale=(0.15, 0.25), name=str(self.win_name) + ".container." + str(name),)



        # for row in range(RULE_ROWS+1):
        #     for column in range(RULE_COLUMNS+1):
        #         Entity(
        #             parent=self.main_containers,
        #             model="circle",
        #             color=color.red,
        #             world_scale=0.5,
        #             x=float(1 / (RULE_COLUMNS+1)) * (row+1) -0.5,
        #             y=float(1 / (RULE_COLUMNS+1)) * (column+1) - 0.5,
        #             z=-10
        #         )








