from ursina import *

TEXT_SPACE = 0.01

class Shop_window(Entity):
    def __init__(self, name:str = "shop") -> None:

        super().__init__()
        self = Entity(parent=camera.ui, 
                             model='quad', 
                             texture=load_texture("/src/window.png"),
                             origin=(0,0),  
                             collider='box',
                             scale_x=1.19,
                             scale_y=0.8)

        cancel = (float(self.scale_x/2), float(self.scale_y/2))

        self.window_name = Text(parent=self, text=name, origin=(0, -0.5), x=0, y=0.3, world_scale=0.01)

        #self.cancel_container = Entity(parent=self, model="circle", origin=(0.5,0.5), scale_x=0.0, scale_y=0.1, x=cancel[0], y=cancel[1])
        self.cancel = Button(parent=self, model="circle", color=color.red, world_scale=0.3, x=-0.415, y=0.377)
        self.cancel.on_click = self.disable

    
    def input(self, key):
        if key == "escape":
            self.disable()

