from UI import app_window
from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton
import json






class Drink_window(app_window.window):
    def __init__(self, coffee_name=None) -> None:
        super().__init__()
        if coffee_name is None:
            self.add_option_button(text="tttttttest")



    def add_option_button(self, text):
        button = Button(
            parent=self,
            name="window.option_button",
            model="circle",
            color=color.gray,
            world_scale=(2, 0.5, 0),
            z=-10,
        )
        text = Text(
            parent=button,
            text=text,
            world_scale=1,
            color=color.white
        )



























































            # DropdownMenu('Material', parent=self.win, x=0, y=0,buttons=(
                
            #     DropdownMenu('Water', buttons=(
            #         DropdownMenuButton('100ml'),
            #         DropdownMenuButton('300ml'),
            #         DropdownMenuButton('500ml'),
            #         DropdownMenuButton('800ml'),
            #         DropdownMenuButton('1000ml'),
            #         )),
            #     DropdownMenu('milk', buttons=(
            #         DropdownMenuButton('100ml'),
            #         DropdownMenuButton('300ml'),
            #         DropdownMenuButton('500ml'),
            #         DropdownMenuButton('800ml'),
            #         DropdownMenuButton('1000ml'),
            #         )),
            #     DropdownMenu('Fruit', buttons=(
            #         DropdownMenuButton('Strawberry'),
            #         DropdownMenuButton('Orange'),
            #         DropdownMenuButton('Peach'),
            #         DropdownMenuButton('Lemon'),
            #         DropdownMenuButton('Lime'),
            #         DropdownMenuButton('Blueberry'),
            #         DropdownMenuButton('Raspberry'),
            #         DropdownMenuButton('Mango'),
            #         DropdownMenuButton('Banana'),
            #         DropdownMenuButton('Pineapple'),
            #         DropdownMenuButton('Grape'),
            #         )),
            #     DropdownMenu('Syrup', buttons=(
            #         DropdownMenuButton("Vanilla Syrup"), 
            #         DropdownMenuButton("Caramel Syrup"), 
            #         DropdownMenuButton("Hazelnut Syrup"), 
            #         DropdownMenuButton("Chocolate Syrup"), 
            #         DropdownMenuButton("Mint Syrup"), 
            #         DropdownMenuButton("Almond Syrup"), 
            #         DropdownMenuButton("Coffee Syrup"), 
            #         DropdownMenuButton("Cinnamon Syrup"), 
            #         DropdownMenuButton("Lemon Syrup"), 
            #         DropdownMenuButton("Raspberry Syrup")
            #         )),
            #     DropdownMenu('etc.', buttons=(
            #         DropdownMenuButton('sugar'),
            #         DropdownMenuButton('cream'),
            #     ))
            # ))




                



