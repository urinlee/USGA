from ursina import *
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
                      x=0.7,
                      collider="box",
                      color=color.light_gray)
        section = [-0.5 + (i/(_MENU_COUNT+1)) for i in range(1, _MENU_COUNT+1)]
        print(section)
        for n in section:
            Button(model='circle', parent=self, origin=(0, 0), world_scale_x=1, world_scale_y=1, y=n) 