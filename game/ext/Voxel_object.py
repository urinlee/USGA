from ursina import *



class Voxel(Button):
    def __init__(self, position=(0, 0, 0), model="cube", texture="white_cube"):
        super().__init__(
            parent=scene,
            position=position,
            model=model,
            texture=texture
        )
    
    