from ursina import *




class Money(Entity):

    def __init__(self):
        super().__init__(parent=camera.ui, 
                      model="quad",
                      scale_x=0.4,
                      scale_y=0.1,
                      origin=(0.5, -0.5),
                      x=-0.5,
                      y=-0.5,
                      color=color.light_gray)
        
        self.money_text = Text(parent=self,origin=(0.5, -0.5), text="100M", world_scale=80)