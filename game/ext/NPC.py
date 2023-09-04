from ursina import *
import threading
import numpy as np

from ext import messaging
from data import npc_message





class npc(Button):
    def __init__(self,name:str, start_pos:Vec3=(18, 1, -29)):
        super().__init__(
            name=f'npc.{random.randint(0, 9999999)}',
            parent=scene,
            model='src/models/person.obj', 
            scale=0.7, 
            rotation_x=-90,
            color=color.red,
            position=start_pos
        )
        #test = Entity(parent=self,
        #              model='src/person.obj',
        #              color=color.blue,
        #              scale=0.8)
        self.npc_name = name
        self.waiting = False
        self.speed = 2
        self.move_x = None
        self.move_z = None
        self.going_home = False
        self.buying = None
        self.seat = None

        self.feel = random.randint(1, 200)

        self.message = None
        self.good_bad = random.randint(0, 200)


    
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
        #print(f"going_home: {self.going_home}  move_x: {self.move_x}  move_z: {self.move_z}")

        if self.move_x:     #움직여야 할 x좌표가 있다면
            normalized = self.move_x / abs(self.move_x)
            move_distance = normalized * time.dt * self.speed
            after = (self.move_x - move_distance) / abs(self.move_x - move_distance)

            if after == normalized:
                self.x += move_distance 
                self.move_x -= move_distance
            else:
                self.x += self.move_x
                self.move_x = None

        if self.going_home and self.move_x is None and self.move_z is None:
            print("delete!")
            self.visible = False
            self.disable()
            del self
            
        elif self.buying is not None and self.move_x is None and self.move_z is None:   #구매중...
            self.buying -= 1
            if self.buying == 0:
                print(self.seat)
                print("nnnot")
                if self.seat is not None:
                    self.move_to(position = self.seat.position)
                else:
                    self.move_to(position = (18, 1, -29))
                    self.going_home = True
                
                messaging.message(entity=self, msg="happy.png", time=2)

        #any(list(filter(lambda a:str(a.name).startswith("object") ,self.collision))):
    
    def wait_counter(self):
        npcs = NPCS()
        count = len(npcs.find_will_waiting()) * 2
        print(11+count)
        del npcs
        self.move_to((11 + count, 1, -8))
        self.waiting = True

        if count/2 >= 4:
            delay_time=float(random.randint(1, 200)/10)

            def main():
                if len(list(NPCS().find_in_waiting())) >= 4:
                    messaging.message(self, msg="anger.png", time=1.5)
                    self.feel -= 20
                
            invoke(main, delay=delay_time)
    



    def go_home(self):
        self.move_to(position = (18, 1, -29))
        self.going_home = True
        



    def move_to(self, position:Vec3):
        print("moving to"+ str(position) + "from" + str(self.position))
        
        self.move_x = Vec3(position).x - self.position.x
        self.move_z = Vec3(position).z - self.position.z
    
    @property
    def is_moving(self):
        return bool((self.move_x !=None and self.move_y!=None ))
    

    def on_click(self):
        self.message = NPC_state(self)
        invoke(self.message.disable, delay=3.0)
    
    

    def messaging(self):
        pass



class NPC_state(Entity):
    def __init__(self, target_NPC:Entity):
        super().__init__(
            name="State_NPC",
            model="quad",
            texture="/../sources/window.png",
            scale=(4, 4, 0.1),
            origin=(0, 0, 0)
        )
        self.target_NPC = target_NPC
        self.message = list(npc_message.messages[self.feel()])
        self.message = str(random.choice(self.message))
        self.message = '\n'.join([' '.join(self.message.split()[i:i+5]) for i in range(0, len(self.message.split()), 5)])


        self.feeling_state = Entity(
            parent=self,
            model="quad",
            name="feeling state",
            texture=f"src/mood/{str(self.feel())}.png",
            scale=0.3,
            origin=(-1, 1, 0),
            x=-0.5,
            y=0.5,
            z=-0.1
        )

        self.feeling_state = Text(
            parent=self,
            name="feeling state_text",
            text='" ' + str(self.message) + ' "',
            color=color.white,
            origin=(0, 0.5, 0),
            scale=2,
            z=-0.1,
            y=-0.1,
            x=0
        )

        

    def update(self):
        self.position = self.target_NPC.position + (0, 6, 0)
        self.look_at(camera.ui)
        self.rotation_z = 0
    
    def input(self, key):
        if key == "q":
            self.disable()
            self.target_NPC.go_home()
            self.target_NPC.speed = 8

    def feel(self):
        if self.target_NPC.feel >= self.target_NPC.good_bad:
            return "happy"
        else:
            return "bad"




class NPCS:
    def __init__(self) -> None:
        self._npc_list=[e for e in scene.entities if str(e.name).startswith("npc")]
    
    def _update_decorator(update_func):
        def wrapper(self, *args, **kwargs):
            self._npc_list = [e for e in scene.entities if str(e.name).startswith("npc")]
            return update_func(self, *args, **kwargs)
        return wrapper
    
    
    @_update_decorator
    def find_by_Name(self, name:str) -> list[npc]:
        finded_npcs = [e for e in self._npc_list if str(e.npc_name) == name]
        return finded_npcs
    

    @_update_decorator
    def find_in_waiting(self, waiting_line_z=-8):
        def _is_waiting(npc):
            a = bool(abs(npc.position.z - waiting_line_z) < 0.01)
            b = bool(npc.waiting)
            c = bool(npc.move_x is None and npc.move_z is None)
            return all([a, b, c])
        
        finded_npcs = [e for e in self._npc_list if _is_waiting(e)]

        if len(finded_npcs) >= 1:
            finded_npcs = list(sorted(finded_npcs, key=lambda a: a.position.x))
        else:
            pass
        return finded_npcs
    
    @_update_decorator
    def find_will_waiting(self):
        finded_npcs = [e for e in self._npc_list if e.waiting]
        return finded_npcs



    


        
        
    
    