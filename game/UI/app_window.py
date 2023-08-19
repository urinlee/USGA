from ursina import *

ITEM_SPACE = 0.1
ITEM_LINE = 2
ITEM_IN_COUNT = 3



class Shop_window_front(Entity):
    black_blind=Entity()
    def invi(self):
        self.back_blind.disable()
        self.disable()


class Shop_window(Entity):

    

    def __init__(self, name:str = "shop") -> None:


        self.back_blind = Entity(parent=camera.ui,
                            model="quad",
                            scale=10,
                            color=color.rgb(0, 0, 0, 180))

        self.win = Entity(parent=camera.ui, 
                             model='quad', 
                             texture=load_texture("/src/window.png"),
                             origin=(0,0),  
                             collider='box',
                             scale_x=1.19,
                             scale_y=0.8)

        #cancel = (float(self.scale_x/2), float(self.scale_y/2))

        self.window_name = Text(parent=self.win, text=name, origin=(0, -0.5), x=0, y=0.3, world_scale=0.01)

        #self.cancel_container = Entity(parent=self, model="circle", origin=(0.5,0.5), scale_x=0.0, scale_y=0.1, x=cancel[0], y=cancel[1])
        self.cancel = Button(parent=self.win, model="circle", color=color.red, world_scale=0.3, x=-0.4145, y=0.376)


        self.cancel.on_click = self.invisibled

        self.item_container = Entity(parent=self.win, model="quad", world_scale_y=10, world_scale_x=15 , color=color.white)

    


    def invisibled(self):
        self.back_blind.disable()
        self.win.disable()
    

    
    def input(self, key):
        print(key)
        if key == "tab":
            self.invisibled()

