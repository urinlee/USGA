from ursina import *

ITEM_SPACE = 0.1
ITEM_LINE = 2
ITEM_IN_COUNT = 3

ALREADY = False



class Shop_window_front(Entity):
    black_blind=Entity()
    def invi(self):
        self.back_blind.disable()
        self.disable()


class window(Entity):

    

    def __init__(self, name:str = "window") -> None:
        self.win_name = name
        self.invisibled()
        
        self.back_blind = Entity(parent=camera.ui,
                            name= name+"." + str(id(super())),
                            model="quad",
                            scale=10,
                            color=color.rgb(0, 0, 0, 180),
                            z=-0.1
                            )

        self.win = Entity(parent=camera.ui, 
                             name= name+"." + str(id(super())),
                             model='quad', 
                             texture=load_texture("/../sources/window.png"),
                             origin=(0,0),  
                             collider='box',
                             scale_x=1.19,
                             scale_y=0.8,
                             z=-0.2)

        #cancel = (float(self.scale_x/2), float(self.scale_y/2))


        #self.cancel_container = Entity(parent=self, model="circle", origin=(0.5,0.5), scale_x=0.0, scale_y=0.1, x=cancel[0], y=cancel[1])

        #취소버튼(red_color, left_top, circle)
        self.cancel = Button(name=name+"." + str(id(super())), parent=self.win, model="circle", color=color.red, world_scale=0.3, x=-0.4145, y=0.376)
        self.cancel.on_click = self.invisibled




        



    def invisibled(self):
        try:
            entities = [i for i in scene.entities if str(i.name).startswith(self.win_name)]
            for n in entities:
                n.disable()
                del n
            
            self.back_blind.disable()
            self.win.disable()
            del self
        except:
            pass
    

    
    def input(self, key):
        print(key)
        if key == "esc":
            self.invisibled()
    


