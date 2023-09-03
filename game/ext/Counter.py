from ursina import *
from ext import NPC, Voxel_object, messaging

import random




NPCS = NPC.NPCS()


class counter(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            name="counter",
            #model="cube",
            #color=color.red,
            colider='box',
            scale=1.5,
            position=(8, 4, -8)
        )
        self.filled_seats = []
        self.processing = None
        self.messaging = None

    # def calc_order(self, target):
    #     def enable():
    #         target.enable()
    #     invoke(enable, delay=10.0)

    def find_to_seat(self) -> Voxel_object.Voxel:
        seats = [e for e in scene.entities if str(e.name).startswith("object") and "chair" in e.name and e not in self.filled_seats]
        
        if len(seats) > 0:
            choiced_seat = random.choice(seats)
            return choiced_seat
        else:
            print("no seats left")
            return None
        

    def calc_buying(self, selected_NPC:NPC.npc, buying_process, seat):
        selected_NPC.buying = buying_process
        selected_NPC.seat = seat



        

    def update(self):
        if len(list(NPCS.find_in_waiting())) > 0 and NPCS.find_in_waiting()[0].position.x < 12:
            NPCS_in_waiting = NPCS.find_in_waiting()
            First_NPC = NPCS_in_waiting[0]
            if First_NPC.buying is None:
                print("First_NPC.buying is None")
                seat = self.find_to_seat()

                self.calc_buying(First_NPC, 1000, seat)
                self.messaging = messaging.message(entity=First_NPC)
                self.processing = NPCS_in_waiting[0]
        
        
        if self.processing is not None and self.processing.buying == 0:
            print("tttttest")
            self.processing.buying = None
            seat = self.processing.seat
            self.filled_seats.append(seat)
            self.processing.waiting = False

            self.messaging.disable()

            for i in NPCS.find_will_waiting():
                if i.move_x is not None:
                    i.move_x -= 2
                    print(f"{i.move_x} -> {i.move_x - 2}")
                else:
                    i.move_x = -2
            self.processing = None
            
            




            # self.calc_order(NPCS_in_waiting[0])

            # if seat is not None:
            #     NPCS_in_waiting[0].move_to(position = seat.position)
            # else:
            #     NPCS_in_waiting[0].move_to(position = (18, 1, -29))
            #     NPCS_in_waiting[0].going_home = True
            
            
            # self.filled_seats.append(seat)
            # NPCS_in_waiting[0].waiting = False
            # for i in NPCS.find_will_waiting():
            #     print(f"{i.move_x} -> {i.move_x - 2}")
            #     i.move_x -= 2
                

