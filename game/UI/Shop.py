from UI import app_window
from ext import player_camera, Voxel_object
from ext.edit_object import Editor
from ursina import *
import json

ITEM_SPACE = 0.1
ITEM_LINE = 2
ITEM_IN_COUNT = 3

with open("game/data/item.json") as item_data_file:
    item_db = json.load(item_data_file)


class shop(app_window.window):
    def __init__(self, number=1):
        super().__init__()
        self.item_container = Entity(name="window.shop." + str(id(super())), parent=self.win, model="quad", world_scale_y=10, world_scale_x=15, color=color.rgb(0, 0, 0, 0))
        self.item_slider = Slider(
            name="window.shop." + str(id(super())), 
            parent=self,
            vertical = True,
            min=1,
            max=int(ceil(len(item_db.keys())/3)),    #최대를 item_db의 key 개수 / 3을 반올림 한 값으로 한다 (ex. item_db.key() = 7: max = 3)
            step=2,
            x=0.5,
            y=-0.25,
            z=-0.3
        )
        def slider_main():
            self.all_clear()
            value = self.item_slider.value
            self.set_item(item_db, num=value)

        self.item_slider.on_value_changed = slider_main
        print(str(ceil(len(item_db.keys())/3)))

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

        self.set_item(item_db, number)




        



    def all_clear(self):

        entities = [i for i in scene.entities if str(i.name).startswith("window.shop.frame.")]
        for n in entities:
            n.disable()
            del n

        # frame = self.frame
        # for num_1, i in enumerate(frame):
        #     for num_2, item in enumerate(frame[num_1]):
        #         print(item)
        #         print(self.frame_item[num_1][num_2])
        #         print(self.frame_item_cost[num_1][num_2])
        #         print("\n\n")

        #         item.visible = False
        #         self.frame_item[num_1][num_2].visible = False
        #         self.frame_item_cost[num_1][num_2].visible = False

        #         item.disable()
        #         self.frame_item[num_1][num_2].disable()
        #         self.frame_item_cost[num_1][num_2].disable()

        self.frame = [[0 for n in range(ITEM_IN_COUNT)]for i in range(ITEM_LINE)]
        self.frame_item = self.frame
        self.frame_item_cost = self.frame

        
        

    def set_item(self, db, num:int = 1):
        for row in range(len(self.item_pos)):
            for column, item in enumerate(self.item_pos[row], 0):
                #number = row * ITEM_IN_COUNT + column
                #print(str(list(db.keys())[number]))

                self.create_item_frame(db, row, column, item, num)


    
    



    def click_item(self, item_name):
        self.invisibled()
        object_item = Voxel_object.Voxel(model=f"src/models/{item_name}", texture=f'src/models/{item_name}.png', position=(0, 1, 0), scale=0.05)
        Editor(object_item)
    
    
        
        


    
    def create_item_frame(self, db, row, column, item, num):
        """
            args:
                db (json.load) : 데이터베이스,
                row (int) : 열
                column (int) : 행
                item (list) : x와 y좌표

            function:
                아이템 칸 1개를 만든다
                
        """
        x = item[0]     #x좌표 설정
        y = item[1]     #y좌표 설정
        number = ITEM_IN_COUNT*(num-1) + row * ITEM_IN_COUNT + column
        print(number)
        try:    #아이템 이름과 가격을 item.json에서 가져오기
            item_name = str(list(db.keys())[number])
            price = db[item_name]["price"]
        except IndexError:  #6개중에 빈공간이 생기면 아이템 이름을 None으로 설정하여 오류를 막음
            item_name = "None"
            price = "None"

        self.frame[row][column] = Button(name="window.shop.frame." + str(id(super())), parent=self.item_container, model="quad",texture="/../sources/item_frame.png" ,x=x, y=y, world_scale=4.8, color=color.dark_gray, highlight_scale=1.1, highlight_color=color.black)    #아이템 프레임 버튼 설정
        self.frame[row][column].on_click = lambda self=self: self.click_item(item_name=item_name)    #버튼 이벤트( 클릭시 편집모드로 돌입 )

        #self.frame[row][column] = frame_button #Frame(shop=self, item_name=item_name, name="shop.frame." + str(id(super())), parent=self.item_container, model="quad",texture="/../sources/item_frame.png" ,x=x, y=y, world_scale=4.8, color=color.dark_gray, highlight_scale=1.1, highlight_color=color.black)  #버튼 세팅 완료
        self.frame_item[row][column] = Entity(name="window.shop.frame." + str(id(super())), parent=self.frame[row][column], model=f"src/models/{item_name}", texture=f'src/models/{item_name}.png', scale=0.01, rotation_x=-20, rotation_y=-30, rotation_z=0, z=-10,y=-0.3) #아이템 사진 엔티티
        self.frame_item_cost[row][column] = Text(name="window.shop.frame." + str(id(super())), parent=self.frame[row][column], text=f"${str(price)}", world_scale=50)     #아이템 가격 Entity





    # def click_category(self, category:str):
    #     self.set_item(item_db[category], category)



    # def set_category(self, num:int = 0):
    #     for row in range(len(self.item_pos)):
    #         for column, item in enumerate(self.item_pos[row], 0):
    #             #number = row * ITEM_IN_COUNT + column
    #             #print(str(list(item_db.keys())[number]))

    #             self.category_frame(item_db, row, column, item)
    #             time.sleep(0.02)
    


    # def category_frame(self, db, row, column, item):
    #     x = item[0]     #x좌표 설정
    #     y = item[1]     #y좌표 설정
    #     number = row * ITEM_IN_COUNT + column
    #     try:
    #         item_name = str(list(db.keys())[number])
    #     except IndexError:
    #         item_name = None

    #     frame_button = Button(parent=self.item_container, model="quad",texture="/../sources/item_frame.png" ,x=x, y=y, world_scale=4.8, color=color.dark_gray, highlight_scale=1.1, highlight_color=color.black)
    #     frame_button.on_click = lambda self=self: self.click_category(item_name)

    #     self.frame[row][column] = frame_button
    #     self.frame_item[row][column] = Entity(parent=self.frame[row][column], model=f"src/{item_name}", texture=f'src/{item_name}.png', scale=0.01, rotation_x=-20, rotation_y=-30, rotation_z=0, z=-10,y=-0.3)


# class Item(Button):
#     def __init__(self, item_name, container, x, y):
#         super().__init__(
#             parent=container, 
#             model="quad",
#             texture="/../sources/item_frame.png",
#             x=x, 
#             y=y, 
#             world_scale=4.8, 
#             color=color.dark_gray, 
#             highlight_scale=1.1, 
#             highlight_color=color.black
#         )
#         self.container = container
#         self.item_name = item_name
    
#     def on_click(self):
#         self.click_item(item_name=self.item_name)
    
#     def click_item(self, item_name):
#         self.container.invisibled()
#         object_item = Voxel_object.Voxel(model=f"src/{item_name}", texture=f'src/{item_name}.png', position=(0, 1, 0), scale=0.05)
#         Editor(object_item)


# class Frame(Button):
#     def __init__(self, shop:shop, item_name, **kwargs):
#         super().__init__(**kwargs)    #아이템 프레임 버튼 설정
#         self.on_click = lambda shop=shop: shop().click_item(item_name)    #버튼 이벤트( 클릭시 편집모드로 돌입 )
        
