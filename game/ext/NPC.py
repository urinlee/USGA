from ursina import *
import threading
import numpy as np





class npc(Button):
    def __init__(self,name:str, start_pos:Vec3=(18, 1, -29)):
        super().__init__(
            name=f'npc.{random.randint(0, 9999999)}',
            parent=scene,
            model='src/person.obj', 
            scale=0.7, 
            rotation_x=-90,
            color=color.red,
            position=start_pos
        )
        #test = Entity(parent=self,
        #              model='src/person.obj',
        #              color=color.blue,
        #              scale=0.8)
        self.speed = 2
        self.move_x = None
        self.move_z = None
    
    def update(self):
        #NPC 움직이는 코드

        if self.move_z:   #움직여야 할 y좌표가 있다면(둘다 있다면 z좌표 먼저)
            normalized = self.move_z / abs(self.move_z)
            move_distance = normalized * time.dt * self.speed
            after = (self.move_z - move_distance) / abs(self.move_z - move_distance)
            
            if after == normalized:
                self.z += move_distance 
                self.move_z -= move_distance
            else:
                self.z += self.move_z
                self.move_z = None

        elif self.move_x:     #움직여야 할 x좌표가 있다면
            normalized = self.move_x / abs(self.move_x)
            move_distance = normalized * time.dt * self.speed
            after = (self.move_x - move_distance) / abs(self.move_x - move_distance)

            if after == normalized:
                self.x += move_distance 
                self.move_x -= move_distance
            else:
                self.x += self.move_x
                self.move_x = None

        



    def move_to(self, position:Vec3):
        print("moving to"+ str(position) + "from" + str(self.position))
        
        self.move_x = Vec3(position).x - self.position.x
        self.move_z = Vec3(position).z - self.position.z
    
    def is_moving(self):
        return bool((self.move_x !=None and self.move_y!=None ))
    


        
        
    
    