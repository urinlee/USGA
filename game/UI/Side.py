from ursina import *
from UI import Shop, player_info, Drink_making, Ruel, about_store
import time

_MENU_COUNT = 6

class Side_Menu(Entity):
    def __init__(self) -> None:
        #메뉴바
        super().__init__(model='quad',
                      name="side_bar",
                      parent=camera.ui,  #2D UI
                      scale=(0.09,0.65),
                      y=0,
                      x=0.85,
                      collider="box",
                      color=color.light_gray)
        section = [-0.5 + (i/(_MENU_COUNT+1)) for i in range(1, _MENU_COUNT+1)]
        self.buttons = [i for i in range(0, _MENU_COUNT)]
        self.already = False

        for num, y_pos in enumerate(section):
            self.buttons[num] = Button(model='circle', parent=self, world_scale_x=1, world_scale_y=1, y=y_pos,color=color.black, highlight_color=color.white) 


        self.buttons[0].on_click = Shop.shop
        self.buttons[1].on_click = Drink_making.Drink_window
        self.buttons[2].on_click = Ruel.Rule_window
        self.buttons[3].on_click = about_store.Room_window


