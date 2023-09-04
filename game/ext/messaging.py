from ursina import *


class message(Entity):
    def __init__(self, entity:Entity, y_up = 4, msg="coffee.png", time:float=None):
        super().__init__(
            model="quad",
            texture="src/message/message.png",
            position=Vec3(entity.position) + Vec3(0, y_up, 0)
        )

        self.entity = entity
        self.y_up = y_up

        if ".png" in msg:
            self.text_message = Entity(
                parent=self,
                model="quad",
                scale=0.5,
                texture="src/message/" + msg,
                origin=(0, -0.2, 0),
                z=-0.005
            )
        else:
            self.text_message = Text(
                parent=self,
                text=msg,
                color=color.black,
                scale=10,
                origin=(0, -0.2, 0),
                z=-0.005
            )
        
        if time is not None:
            invoke(self.disable, delay=float(time))
    
    def update(self):
        self.position = Vec3(self.entity.position) + Vec3(0, self.y_up, 0)
        self.look_at(camera.ui)
    
    def disable(self):
        super().disable()
    
    