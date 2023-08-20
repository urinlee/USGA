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
                             texture=load_texture("/../sources/window.png"),
                             origin=(0,0),  
                             collider='box',
                             scale_x=1.19,
                             scale_y=0.8)

        #cancel = (float(self.scale_x/2), float(self.scale_y/2))


        #self.cancel_container = Entity(parent=self, model="circle", origin=(0.5,0.5), scale_x=0.0, scale_y=0.1, x=cancel[0], y=cancel[1])

        #취소버튼(red_color, left_top, circle)
        self.cancel = Button(parent=self.win, model="circle", color=color.red, world_scale=0.3, x=-0.4145, y=0.376)
        self.cancel.on_click = self.invisibled


        self.item_container = Entity(parent=self.win, model="quad", world_scale_y=10, world_scale_x=15, color=color.rgb(0, 0, 0, 0))

        #self.test_pos = Entity(parent=self.item_container, model="quad", x=0.5, y=0.5, scale=0.01, color=color.red)

        self.item_pos = [[n for n in range(ITEM_IN_COUNT)]for i in range(ITEM_LINE)]

        print(self.item_pos)    

        for num, section in enumerate(self.item_pos, 0):
            self.item_pos[num] = list(map(lambda a: (
                                                    round(-0.5 + ((a+0.5)/(len(section))), 10) , 
                                                    round(0.5-((num+0.5)/(len(self.item_pos))), 10)), 
                                                    section))
        print(self.item_pos)

        for row in range(len(self.item_pos)):
            for item in self.item_pos[row]:
                x = item[0]
                y = item[1]

                b = Button(parent=self.item_container, model="quad",texture="/../sources/item_frame.png" ,x=x, y=y, world_scale=4.8, origin=(0, 0), color=color.dark_gray, highlight_scale=1.1, highlight_color=color.black)
                e = Entity(parent=b, model="cube", texture="white_cube", scale=0.5, rotation_x=45, rotation_y=30)
                print(f"test  {x},{y}")
        

    


    def invisibled(self):
        self.back_blind.disable()
        self.win.disable()
    

    
    def input(self, key):
        print(key)
        if key == "tab":
            self.invisibled()

