from UI import app_window
from ursina import *
import json

ITEM_SPACE = 0.1
ITEM_LINE = 2
ITEM_IN_COUNT = 3


class shop(app_window.window):
    def __init__(self):
        super().__init__()
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

        self.frame = [[0 for n in range(ITEM_IN_COUNT)]for i in range(ITEM_LINE)]
        self.frame_item = self.frame
        self.frame_item_cost = self.frame

        self.set_item()

        
        

    def set_item(self, num:int = 0):
        with open("game/data/item.json") as item_data_file:
            item_db = json.load(item_data_file)
        for row in range(len(self.item_pos)):
            for column, item in enumerate(self.item_pos[row], 0):
                number = row * ITEM_IN_COUNT + column
                print(str(list(item_db.keys())[number]))

                self.item_frame(item_db, row, column, item)
                time.sleep(0.02)


    
    def item_frame(self,item_db, row, column, item):
        x = item[0]
        y = item[1]
        number = row * ITEM_IN_COUNT + column
        item_name = str(list(item_db.keys())[number])
        price = item_db[item_name]["price"]

        frame_button = Button(parent=self.item_container, model="quad",texture="/../sources/item_frame.png" ,x=x, y=y, world_scale=4.8, color=color.dark_gray, highlight_scale=1.1, highlight_color=color.black)
        frame_button.on_click = self.invisibled

        self.frame[row][column] = frame_button
        self.frame_item[row][column] = Entity(parent=self.frame[row][column], model=f"src/{item_name}", texture=f'src/{item_name}.png', scale=0.01, rotation_x=-20, rotation_y=-30, rotation_z=0, z=-10,y=-0.3)
        self.frame_item_cost[row][column] = Text(parent=self.frame[row][column], text=f"${str(price)}", world_scale=50)

    
