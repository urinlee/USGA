from ursina import *


class message(Entity):
    def __init__(self, entity:Entity, y_up = 4, msg="coffee.png"):
        super().__init__(
            model="quad",
            texture="src/message.png",
            position=Vec3(entity.position) + Vec3(0, y_up, 0)
        )

        self.entity = entity
        self.y_up = y_up

        if ".png" in msg:
            self.text_message = Entity(
                parent=self,
                model="quad",
                scale=0.5,
                texture=msg,
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
    
    def update(self):
        self.position = Vec3(self.entity.position) + Vec3(0, self.y_up, 0)
        self.look_at(camera.ui)
    
    