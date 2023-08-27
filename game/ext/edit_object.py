from ursina import *
from ext.Voxel_object import Voxel


STOP_ROTATION=list(map(float, [-45, -90, -135, -180, -225, -270, -315, -360, 0, 45, 90, 135, 180, 225, 270, 315, 360]))
max_rotation_guide = 50
rotate_speed = 0.5


class Editor(Entity):
    def __init__(self, object:Voxel):
        super().__init__()
        self.object = object
        self.rotation_guide = 0
        mouse.enabled = True
        self.guide = Button(parent=scene, model="cube", position=(0, 0.1, 0), scale=(30, 1, 30), origin=(-0.5, -0.5, 0.5), visible=False)
        self.object.hovered=False
        
        
        


    def update(self):

        if held_keys["e"]:      #object rotate
            print(self.object.rotation_y)
            if self.object.rotation_y in STOP_ROTATION and self.rotation_guide < max_rotation_guide:
                self.rotation_guide += 1
                if self.object.rotation_y == 360:
                    self.object.rotation_y = 0

            elif self.rotation_guide>=max_rotation_guide:
                print("ttest")
                self.rotation_guide = 0
                self.object.rotation_y += rotate_speed
            else:
                self.object.rotation_y += rotate_speed
                self.object.rotation_y = round(self.object.rotation_y, 1)
        
        if held_keys["q"]:      #object rotate
            print(self.object.rotation_y)
            if self.object.rotation_y in STOP_ROTATION and self.rotation_guide < max_rotation_guide:
                self.rotation_guide += 1
                if self.object.rotation_y == -360:
                    self.object.rotation_y = 360

            elif self.rotation_guide>=max_rotation_guide:
                print("ttest")
                self.rotation_guide = 0
                self.object.rotation_y -= rotate_speed
            else:
                self.object.rotation_y -= rotate_speed
                self.object.rotation_y = round(self.object.rotation_y, 1)

            
        mouse_position = mouse.point
        # 마우스의 현재 위치 가져오기
        if mouse_position is not None:
            for entity in mouse.collisions:
                if entity.entity == self.guide:
                    self.object.x = entity.point[0] * 30
                    self.object.z = entity.point[2] * 30


        self.position = mouse_position

        
        
        

        
    

    def input(self, key):
        if key == "space" or key == "left mouse down":
            self.guide.disable()
            self.disable()
        

        
            
            
            

        # if key == "r":
        #     print("test")
        #     self.object.rotation_y += 10\
