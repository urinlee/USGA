from ursina import *



class Voxel(Button):
    def __init__(self, position=(0, 10, 0), model="cube", texture="white_cube", scale:Vec3|int =(1, 1, 1)):
        super().__init__(
            name=f"object.{model}.{random.randint(0, 9999999)})",
            parent=scene,
            position=position,
            model=model,
            texture=load_texture(texture),
            scale = scale,
            color=color.color(0, 0, 1),
            collider="cube",
            origin = (-12.5, 0, 12.5)
        )
        print("make")
        print(self.position)

    
    
    
    
    