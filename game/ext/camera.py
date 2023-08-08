from ursina import *

#Camera
class Camera(EditorCamera):
    def __init__(self, speed = 0.05, start_position = (0, 10, 0)):  #생성자
        super().__init__()
        self.move_speed = 0,
        self.rotation_speed = 0,
        self.rotation = (45, -45)
        self.start_position = start_position
        self.speed = speed


    def update(self):
        try:
            super().update()
        except:
            pass
        if held_keys["w"]:
            self.x -= self.speed
            self.z += self.speed
        
        if held_keys["s"]:
            self.x += self.speed
            self.z -= self.speed
        
        if held_keys["d"]:
            self.x += self.speed
            self.z += self.speed
        
        if held_keys["a"]:
            self.x -= self.speed
            self.z -= self.speed
